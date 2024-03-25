class Controls:
    def __init__(self, game):
        self.funcs = {
            "volume_up": lambda x: self.volume_up(x),
            "volume_down": lambda x: self.volume_down(x),
        }
        self.game = game

    def volume_up(self, value):
        self.game.volume -= float(value)
        self.game.volume = round(min(max(self.game.volume, 0), 1), 2)
        self.game.save_options()

    def volume_down(self, value):
        self.game.volume += float(value)
        self.game.volume = round(min(max(self.game.volume, 0), 1), 2)
        self.game.save_options()
