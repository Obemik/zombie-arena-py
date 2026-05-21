from dataclasses import dataclass, field
from typing import Optional

from core.weapons import Weapon


@dataclass
class Entity:
	name: str
	hp: int
	damage: int
	max_hp: int = field(init=False)

	def __post_init__(self) -> None:
		self.hp = int(max(0, self.hp))
		self.damage = int(max(0, self.damage))
		self.max_hp = self.hp

	@property
	def is_alive(self) -> bool:
		return self.hp > 0

	def take_damage(self, amount: int) -> int:
		value = int(max(0, amount))
		self.hp = max(0, self.hp - value)
		return value

	def heal(self, amount: int) -> int:
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
	inventory: list[Weapon] = field(default_factory=list)

	@property
	def attack_damage(self) -> int:
		if self.weapon is not None:
			return self.weapon.damage
		return self.damage

	def attack(self, target: Entity, multiplier: float = 1.0) -> int:
		raw = int(self.attack_damage * max(0.0, multiplier))
		return target.take_damage(raw)

	def can_buy(self, weapon: Weapon) -> bool:
		return self.money >= weapon.cost

	def buy_weapon(self, weapon: Weapon) -> bool:
		if not self.can_buy(weapon):
			return False
		self.money -= weapon.cost
		self.inventory.append(weapon)
		self.weapon = weapon
		return True

	def add_money(self, amount: int) -> None:
		self.money += int(max(0, amount))


@dataclass
class Zombie(Entity):
	reward: int = 0

	def attack(self, target: Entity) -> int:
		return target.take_damage(self.damage)
