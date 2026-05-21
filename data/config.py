PLAYER_NAME = "Player"
PLAYER_HP = 100
PLAYER_DAMAGE = 10
PLAYER_START_MONEY = 50
ROUND_REWARD = 20
HEAL_COST = 15
HEAL_AMOUNT = 25

ARENA_WIDTH = 20
ARENA_HEIGHT = 10
TICK_RATE = 10
SCORE_PER_KILL = 5
WAVE_ENEMY_BASE = 3
WAVE_ENEMY_GROWTH = 2

WEAPON_SHOP = {
    "knife":   {"name": "Knife",   "damage": 12, "cost": 0},
    "bat":     {"name": "Bat",     "damage": 18, "cost": 35},
    "pistol":  {"name": "Pistol",  "damage": 25, "cost": 70},
    "shotgun": {"name": "Shotgun", "damage": 40, "cost": 120},
}

SHOP_ITEMS = [
    {"weapon_id": "knife",   "name": "Knife",   "cost": 0,   "desc": "Базова зброя"},
    {"weapon_id": "bat",     "name": "Bat",     "cost": 35,  "desc": "Більше шкоди"},
    {"weapon_id": "pistol",  "name": "Pistol",  "cost": 70,  "desc": "Гарний вибір"},
    {"weapon_id": "shotgun", "name": "Shotgun", "cost": 120, "desc": "Найсильніша"},
]

ENEMY_TYPES = {
    "walker": {"name": "Walker", "hp": 35,  "damage": 7,  "reward": 10},
    "runner": {"name": "Runner", "hp": 25,  "damage": 11, "reward": 12},
    "tank":   {"name": "Tank",   "hp": 70,  "damage": 9,  "reward": 18},
    "boss":   {"name": "Boss",   "hp": 140, "damage": 16, "reward": 35},
}

WAVE_ENEMY_POOL = ["walker", "walker", "runner", "tank"]