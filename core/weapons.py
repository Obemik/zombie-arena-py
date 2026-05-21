from dataclasses import dataclass


@dataclass
class Weapon:
	name: str
	damage: int
	cost: int

	def __post_init__(self) -> None:
		self.damage = int(max(0, self.damage))
		self.cost = int(max(0, self.cost))


def create_weapon(name: str, damage: int, cost: int) -> Weapon:
	return Weapon(name=name, damage=damage, cost=cost)
