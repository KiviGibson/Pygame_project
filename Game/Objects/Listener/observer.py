import Game.Objects.Listener.listener as listener


class Observer:
    def __init__(self, *events):
        self.events = {}
        for event in events:
            self.events[event] = []

    def add_event(self, function):
        ...

    def remove_listener(self, event, func):
        self.events[event].remove(func)

    def add_listener(self):
        ...

    def activate_event(self, name):
        if name in self.events:
            for func in self.events[name]:
                func()
    