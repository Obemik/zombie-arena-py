from abc import ABC, abstractmethod
from core.entities import Player, Zombie


class Command(ABC):
    @abstractmethod
    def execute(self, arena=None):
        pass


class MoveCommand(Command):
    def __init__(self, player, dx, dy):
        self.player = player
        self.dx = dx
        self.dy = dy

    def execute(self, arena=None):
        new_x = self.player.position.x + self.dx
        new_y = self.player.position.y + self.dy
        if arena and arena.is_free(new_x, new_y):
            arena.place(self.player, new_x, new_y)


class AttackCommand(Command):
    def __init__(self, player, enemies, bus, arena):
        self.player = player
        self.enemies = enemies
        self.bus = bus
        self.arena = arena

    def execute(self, arena=None):
        best = None
        best_dist = 999
        for enemy in self.enemies:
            dist = self.player.position.distance_to(enemy.position)
            if dist < best_dist:
                best_dist = dist
                best = enemy
        if best and best_dist <= 3.0:
            dmg = self.player.attack_damage
            best.take_damage(dmg)
            self.bus.push_log("Атака! " + str(dmg) + " шкоди, HP зомбі: " + str(best.hp))


class BuyWeaponCommand(Command):
    def __init__(self, player, weapon):
        self.player = player
        self.weapon = weapon

    def execute(self, arena=None):
        return self.player.buy_weapon(self.weapon)


class HealCommand(Command):
    def __init__(self, target, amount):
        self.target = target
        self.amount = amount

    def execute(self, arena=None):
        return self.target.heal(self.amount)


class PauseCommand(Command):
    def __init__(self, engine):
        self.engine = engine

    def execute(self, arena=None):
        from patterns.state import PausedState
        self.engine.set_state(PausedState())