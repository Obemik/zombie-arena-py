import time
import random
from core.arena import Arena, Position
from patterns.observer import EventBus, LogObserver
from patterns.state import PlayingState, ShopState, GameOverState, PausedState
from patterns.factory import EnemyFactory, WeaponFactory
from patterns.command import MoveCommand, AttackCommand, PauseCommand
from data.config import TICK_RATE, SHOP_ITEMS, SCORE_PER_KILL, WAVE_ENEMY_BASE, WAVE_ENEMY_GROWTH, WAVE_ENEMY_POOL


class GameEngine:
    def __init__(self, player, renderer, input_handler):
        self.player = player
        self.renderer = renderer
        self.input_handler = input_handler
        self.arena = Arena()
        self.bus = EventBus()
        self.log_observer = LogObserver(self.bus)
        self.bus.subscribe(self.log_observer)
        self.enemies = []
        self.wave = 1
        self.score = 0
        self.running = True
        self.state = PlayingState()
        self.shop_cursor = 0
        self.player.position = Position(self.arena.width // 2, self.arena.height // 2)
        self.arena.cells[(self.player.position.x, self.player.position.y)] = self.player
        self._spawn_wave()

    def set_state(self, state):
        self.state = state

    def run(self):
        while self.running:
            self.state.update(self)
            self.renderer.render(self)
            time.sleep(1.0 / TICK_RATE)

    def update_playing(self):
        key = self.input_handler.get_key()
        if key:
            self._handle_key(key)
        self._move_enemies()
        self._check_enemy_attacks()
        if not self.player.is_alive:
            self.bus.notify("player_died", {})
            self.set_state(GameOverState())
            return
        if len(self.enemies) == 0:
            self.set_state(ShopState())
            self.bus.notify("shop_open", {})

    def update_shop(self):
        key = self.input_handler.get_key()
        if key == "up":
            self.shop_cursor = (self.shop_cursor - 1) % len(SHOP_ITEMS)
        elif key == "down":
            self.shop_cursor = (self.shop_cursor + 1) % len(SHOP_ITEMS)
        elif key == "enter":
            self._buy_item(self.shop_cursor)
        elif key == "q":
            self.wave += 1
            self._spawn_wave()
            self.set_state(PlayingState())
            self.bus.notify("wave_start", {"wave": self.wave})

    def update_game_over(self):
        key = self.input_handler.get_key()
        if key == "q":
            self.running = False

    def update_paused(self):
        key = self.input_handler.get_key()
        if key == "p":
            self.set_state(PlayingState())

    def _handle_key(self, key):
        commands = {
            "up":    MoveCommand(self.player, 0, -1),
            "down":  MoveCommand(self.player, 0, 1),
            "left":  MoveCommand(self.player, -1, 0),
            "right": MoveCommand(self.player, 1, 0),
            "e":     AttackCommand(self.player, self.enemies, self.bus, self.arena),
            "p":     PauseCommand(self),
        }
        if key in commands:
            commands[key].execute(self.arena)

    def _move_enemies(self):
        for enemy in self.enemies:
            enemy.move_towards(self.player.position, self.arena)

    def _check_enemy_attacks(self):
        for enemy in list(self.enemies):
            dist = enemy.position.distance_to(self.player.position)
            if dist <= 1.5:
                if not hasattr(enemy, 'attack_cooldown'):
                    enemy.attack_cooldown = 0
                if enemy.attack_cooldown <= 0:
                    dmg = enemy.damage
                    self.player.take_damage(dmg)
                    self.bus.notify("player_hit", {"damage": dmg})
                    enemy.attack_cooldown = 3
                else:
                    enemy.attack_cooldown -= 1

        dead = [e for e in self.enemies if not e.is_alive]
        for e in dead:
            self.arena.remove(e)
            self.enemies.remove(e)
            self.score += SCORE_PER_KILL
            self.bus.notify("enemy_killed", {"score": SCORE_PER_KILL})
            self.player.add_money(e.reward)

    def _spawn_wave(self):
        count = WAVE_ENEMY_BASE + (self.wave - 1) * WAVE_ENEMY_GROWTH
        for _ in range(count):
            pos = self.arena.get_free_spawn_point()
            if pos is None:
                break
            enemy_key = random.choice(WAVE_ENEMY_POOL)
            enemy = EnemyFactory.create(enemy_key)
            enemy.position = Position(pos[0], pos[1])
            self.arena.cells[(pos[0], pos[1])] = enemy
            self.enemies.append(enemy)

    def _buy_item(self, index):
        if index >= len(SHOP_ITEMS):
            return
        item = SHOP_ITEMS[index]
        if self.player.money >= item["cost"]:
            weapon = WeaponFactory.create(item["weapon_id"])
            self.player.buy_weapon(weapon)
            self.bus.notify("weapon_bought", {"name": weapon.name})