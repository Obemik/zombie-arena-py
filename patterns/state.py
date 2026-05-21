from abc import ABC, abstractmethod


class GameState(ABC):
    @abstractmethod
    def update(self, engine):
        pass

    @abstractmethod
    def get_name(self):
        pass


class PlayingState(GameState):
    def update(self, engine):
        engine.update_playing()

    def get_name(self):
        return "playing"


class ShopState(GameState):
    def update(self, engine):
        engine.update_shop()

    def get_name(self):
        return "shop"


class GameOverState(GameState):
    def update(self, engine):
        engine.update_game_over()

    def get_name(self):
        return "game_over"


class PausedState(GameState):
    def update(self, engine):
        engine.update_paused()

    def get_name(self):
        return "paused"