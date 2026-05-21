from core.interfaces import GameObserver, GameSubject


class EventBus(GameSubject):
    def __init__(self):
        self._observers: list[GameObserver] = []
        self._log: list[str] = []

    def subscribe(self, observer: GameObserver):
        self._observers.append(observer)

    def unsubscribe(self, observer: GameObserver):
        self._observers.remove(observer)

    def notify(self, event_type: str, data: dict):
        for observer in self._observers:
            observer.on_event(event_type, data)

    def get_log(self) -> list[str]:
        return self._log

    def push_log(self, message: str):
        self._log.append(message)
        if len(self._log) > 8:
            self._log.pop(0)


class LogObserver(GameObserver):
    def __init__(self, bus: EventBus):
        self.bus = bus

    def on_event(self, event_type: str, data: dict):
        if event_type == "enemy_killed":
            self.bus.push_log(f"Ворога вбито! +{data.get('score', 0)} очок")
        elif event_type == "player_hit":
            self.bus.push_log(f"Гравець отримав {data.get('damage', 0)} шкоди")
        elif event_type == "wave_start":
            self.bus.push_log(f"Хвиля {data.get('wave', 1)} починається!")
        elif event_type == "weapon_bought":
            self.bus.push_log(f"Куплено: {data.get('name', '')}")
        elif event_type == "player_died":
            self.bus.push_log("Гравець загинув!")
        elif event_type == "shop_open":
            self.bus.push_log("Магазин відкрито. Обери зброю.")