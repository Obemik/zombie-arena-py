from abc import ABC, abstractmethod

from core.entities import Entity, Player
from core.weapons import Weapon
from patterns.strategy import AttackStrategy, NormalAttackStrategy


class Command(ABC):
	@abstractmethod
	def execute(self):
		raise NotImplementedError


class AttackCommand(Command):
	def __init__(self, attacker: Player, target: Entity, strategy: AttackStrategy | None = None) -> None:
		self.attacker = attacker
		self.target = target
		self.strategy = strategy or NormalAttackStrategy()

	def execute(self) -> int:
		return self.attacker.attack(self.target, self.strategy.get_multiplier())


class BuyWeaponCommand(Command):
	def __init__(self, player: Player, weapon: Weapon) -> None:
		self.player = player
		self.weapon = weapon

	def execute(self) -> bool:
		return self.player.buy_weapon(self.weapon)


class HealCommand(Command):
	def __init__(self, target: Entity, amount: int) -> None:
		self.target = target
		self.amount = amount

	def execute(self) -> int:
		return self.target.heal(self.amount)
