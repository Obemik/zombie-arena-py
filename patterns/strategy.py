import random
from abc import ABC, abstractmethod


class AttackStrategy(ABC):
	@abstractmethod
	def get_multiplier(self) -> float:
		raise NotImplementedError


class NormalAttackStrategy(AttackStrategy):
	def get_multiplier(self) -> float:
		return 1.0


class CriticalAttackStrategy(AttackStrategy):
	def __init__(self, crit_chance: float = 0.25, crit_multiplier: float = 2.0) -> None:
		self.crit_chance = max(0.0, min(1.0, crit_chance))
		self.crit_multiplier = max(1.0, crit_multiplier)

	def get_multiplier(self) -> float:
		if random.random() < self.crit_chance:
			return self.crit_multiplier
		return 1.0


class LowAttackStrategy(AttackStrategy):
	def __init__(self, factor: float = 0.7) -> None:
		self.factor = max(0.0, min(1.0, factor))

	def get_multiplier(self) -> float:
		return self.factor
