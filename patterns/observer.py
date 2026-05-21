from core.interfaces import GameObserver, GameSubject


class EventBus(GameSubject):
    def __init__(self):
        self._observers = []
        self._log = []

    def subscribe(self, observer):
        self._observers.append(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, event_type, data):
        for observer in self._observers:
            observer.on_event(event_type, data)

    def get_log(self):
        return self._log

    def push_log(self, message):
        self._log.append(message)
        if len(self._log) > 8:
            self._log.pop(0)


class LogObserver(GameObserver):
    def __init__(self, bus):
        self.bus = bus

    def on_event(self, event_type, data):
        if event_type == "enemy_killed":
            self.bus.push_log("Ворога вбито! +" + str(data.get("score", 0)) + " очок")
        elif event_type == "player_hit":
            self.bus.push_log("Гравець отримав " + str(data.get("damage", 0)) + " шкоди")
        elif event_type == "wave_start":
            self.bus.push_log("Хвиля " + str(data.get("wave", 1)) + " починається!")
        elif event_type == "weapon_bought":
            self.bus.push_log("Куплено: " + str(data.get("name", "")))
        elif event_type == "player_died":
            self.bus.push_log("Гравець загинув!")
        elif event_type == "shop_open":
            self.bus.push_log("Магазин відкрито. Обери зброю.")