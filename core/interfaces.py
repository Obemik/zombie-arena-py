from abc import ABC, abstractmethod


class Drawable(ABC):
    @abstractmethod
    def get_symbol(self):
        pass


class Damageable(ABC):
    @abstractmethod
    def take_damage(self, amount):
        pass

    @abstractmethod
    def is_alive(self):
        pass


class Movable(ABC):
    @abstractmethod
    def move(self, dx, dy):
        pass


class GameObserver(ABC):
    @abstractmethod
    def on_event(self, event_type, data):
        pass


class GameSubject(ABC):
    @abstractmethod
    def subscribe(self, observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        pass

    @abstractmethod
    def notify(self, event_type, data):
        pass