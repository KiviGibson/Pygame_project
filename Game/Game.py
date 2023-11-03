from pygame import *
import Options as gameOption


class Game:
    def __init__(self):
        init()
        self.running = True
        self.option = gameOption.Option("Game Title", "", (500, 600))
        self.clock = time.Clock()
        self.gameobjects = []
        self.userobjects = []

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
            self.clock.tick(70)
            self.refresh()

    @staticmethod
    def refresh():
        display.flip()
        display.get_surface().fill((20, 20, 20))

    def startup(self):
        option = self.option
        display.set_mode(option.size)

        screen = display.get_surface()
        basecolor = (20, 20, 20)
        screen.fill(basecolor)

        display.set_caption(option.title)

        if option.icon:
            icon = image.load(option.icon)
            display.set_icon(icon)

    def addobject(self, gameobject):
        self.gameobjects.append(gameobject)

    def adduserobject(self, gameobject):
        self.userobjects.append(gameobject)
