from pygame import *
import Game.Options as gameOption


class Game:
    def __init__(self, tickrate=60, size=(400,500), name="Game Title", img=""):
        init()
        self.running = True
        self.option = gameOption.Option(name, img, size, tickrate)
        option = self.option
        self.clock = time.Clock()
        self.gameobjects = []
        self.userobjects = []
        display.set_mode(option.size)

        display.set_caption(option.title)

        if option.icon:
            icon = image.load(option.icon)
            display.set_icon(icon)
    def start(self):
        while self.running:
            for e in event.get():
                for players in self.userobjects:
                    players.input.event(e)
                if e.type == QUIT:
                    self.running = False
            for players in self.userobjects:
                players.walk(mult=self.clock.get_fps()*0.01)
            for entity in self.gameobjects:
                entity.draw()
            self.clock.tick(self.option.tickrate)
            self.refresh()

    def refresh(self):
        display.flip()
        display.get_surface().fill(self.option.color)

    def addobject(self, gameobject):
        self.gameobjects.append(gameobject)

    def adduserobject(self, gameobject):
        self.userobjects.append(gameobject)
