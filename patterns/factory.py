from core.entities import Zombie
from core.weapons import Weapon
from data.config import ENEMY_TYPES, WEAPON_SHOP


class WeaponFactory:
	@staticmethod
	def create(weapon_key: str) -> Weapon:
		key = weapon_key.lower()
		if key not in WEAPON_SHOP:
			raise ValueError(f"Unknown weapon: {weapon_key}")
		data = WEAPON_SHOP[key]
		return Weapon(name=data["name"], damage=data["damage"], cost=data["cost"])


class EnemyFactory:
	@staticmethod
	def create(enemy_key: str) -> Zombie:
		key = enemy_key.lower()
		if key not in ENEMY_TYPES:
			raise ValueError(f"Unknown enemy: {enemy_key}")
		data = ENEMY_TYPES[key]
		return Zombie(name=data["name"], hp=data["hp"], damage=data["damage"], reward=data["reward"])
