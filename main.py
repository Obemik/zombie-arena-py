from core.entities import Player
from ui.renderer import ConsoleRenderer
from ui.input_handler import InputHandler
from core.engine import GameEngine
from data.config import PLAYER_HP


def main():
    print("Zombie Arena")
    print("Виживи проти нескінченних хвиль зомбі!")
    input("Натисни Enter щоб почати...")
    player = Player("Hero", PLAYER_HP)
    renderer = ConsoleRenderer()
    handler = InputHandler()
    engine = GameEngine(player, renderer, handler)
    engine.run()


if __name__ == "__main__":
    main()