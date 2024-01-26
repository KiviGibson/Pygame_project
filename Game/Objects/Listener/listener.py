import Game.Objects.Listener.observer as observer


class Listener:
    def __init__(self, *events: list[int, str, any]):
        self.subscribed: list[dict[:observer.Observer, :str, :any]] = []
        for event in events:
            self.subscribe(*event)

    def subscribe(self, obj: object, event: str, func: any):
        if not self.check_observer(obj):
            return
        obj.observer.events[event].append(func)
        self.subscribed.append({"o": obj.observer, "e": event, "f": func})

    def unsubnscribe(self, observer=None, event="", func=None, index=-1):
        if (i:= index) > -1:
            o: observer.Observer = self.subscribed[i]["o"]
            o.remove_listener(self.subscribed[i]["e"], self.subscribed[i]["f"])
        else:
            try:
                observer.remove_listener(event, func)
            except:
                raise Exception("Cant unsubscribe this func!")

    def check_observer(self, obj: object) -> bool:
        try:
            return obj.observer.test()
        except AttributeError:
            return False
