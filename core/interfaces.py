from abc import ABC, abstractmethod


class Drawable(ABC):
    @abstractmethod
    def get_symbol(self) -> str:
        pass


class Damageable(ABC):
    @abstractmethod
    def take_damage(self, amount: int):
        pass

    @abstractmethod
    def is_alive(self) -> bool:
        pass


class Movable(ABC):
    @abstractmethod
    def move(self, dx: int, dy: int):
        pass


class GameObserver(ABC):
    @abstractmethod
    def on_event(self, event_type: str, data: dict):
        pass


class GameSubject(ABC):
    @abstractmethod
    def subscribe(self, observer: GameObserver):
        pass

    @abstractmethod
    def unsubscribe(self, observer: GameObserver):
        pass

    @abstractmethod
    def notify(self, event_type: str, data: dict):
        pass