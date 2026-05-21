from dataclasses import dataclass, field
from typing import Optional
from core.weapons import Weapon


@dataclass
class Entity:
    name: str
    hp: int
    damage: int
    max_hp: int = field(init=False)

    def __post_init__(self):
        self.hp = int(max(0, self.hp))
        self.damage = int(max(0, self.damage))
        self.max_hp = self.hp

    @property
    def is_alive(self):
        return self.hp > 0

    def take_damage(self, amount):
        value = int(max(0, amount))
        self.hp = max(0, self.hp - value)
        return value

    def heal(self, amount):
        if not self.is_alive:
            return 0
        value = int(max(0, amount))
        before = self.hp
        self.hp = min(self.max_hp, self.hp + value)
        return self.hp - before


@dataclass
class Player(Entity):
    money: int = 0
    weapon: Optional[Weapon] = None
    inventory: list = field(default_factory=list)
    position: object = field(default=None, init=False)

    @property
    def attack_damage(self):
        if self.weapon is not None:
            return self.weapon.damage
        return self.damage

    def attack(self, target, multiplier=1.0):
        raw = int(self.attack_damage * max(0.0, multiplier))
        return target.take_damage(raw)

    def can_buy(self, weapon):
        return self.money >= weapon.cost

    def buy_weapon(self, weapon):
        if not self.can_buy(weapon):
            return False
        self.money -= weapon.cost
        self.inventory.append(weapon)
        self.weapon = weapon
        return True

    def add_money(self, amount):
        self.money += int(max(0, amount))

    def get_symbol(self):
        return "@"


@dataclass
class Zombie(Entity):
    reward: int = 0
    position: object = field(default=None, init=False)

    def attack(self, target):
        return target.take_damage(self.damage)

    def get_symbol(self):
        return "Z"

    def move_towards(self, target_pos, arena):
        dx = 0
        dy = 0
        if target_pos.x > self.position.x:
            dx = 1
        elif target_pos.x < self.position.x:
            dx = -1
        if target_pos.y > self.position.y:
            dy = 1
        elif target_pos.y < self.position.y:
            dy = -1
        if dx != 0 and arena.is_free(self.position.x + dx, self.position.y):
            arena.place(self, self.position.x + dx, self.position.y)
        elif dy != 0 and arena.is_free(self.position.x, self.position.y + dy):
            arena.place(self, self.position.x, self.position.y + dy)