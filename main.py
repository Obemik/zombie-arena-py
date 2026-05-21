from core.entities import Player
from ui.renderer import ConsoleRenderer
from ui.input_handler import InputHandler
from core.engine import GameEngine
from data.config import PLAYER_NAME, PLAYER_HP, PLAYER_DAMAGE, PLAYER_START_MONEY
from core.weapons import Weapon


def main():
    print("Zombie Arena")
    print("Виживи проти нескінченних хвиль зомбі!")
    input("Натисни Enter щоб почати...")
    player = Player(name=PLAYER_NAME, hp=PLAYER_HP, damage=PLAYER_DAMAGE, money=PLAYER_START_MONEY)
    starter_weapon = Weapon(name="Knife", damage=12, cost=0)
    player.weapon = starter_weapon
    renderer = ConsoleRenderer()
    handler = InputHandler()
    engine = GameEngine(player, renderer, handler)
    engine.run()


if __name__ == "__main__":
    main()