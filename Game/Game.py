from pygame import *
import pygame
from Game import options, map

class Game:
    def __init__(self, tickrate=60, size=(400, 500), name="Game Title", img=""):
        init()
        self.running = True
        self.option = options.Option(name, img, size, tickrate)
        self.clock = time.Clock()
        self.gameobjects = []
        self.userobjects = []
        self.events = []
        self.moving_sprites = pygame.sprite.Group()
        option = self.option
        display.set_mode(option.size)
        display.set_caption(option.title)
        self.map = map.Map()

        if option.icon:
            icon = image.load(option.icon)
            display.set_icon(icon)

    def setup(self):
        self.createmap()
        for entity in self.gameobjects:
            entity.start(self)
            self.moving_sprites.add(entity)

    def start(self):
        self.setup()
        while self.running:
            self.events.clear()
            for e in event.get():
                if e.type == QUIT:
                    self.running = False
                self.events.append(e)
            for entity in self.gameobjects:
                entity.update()
            self.moving_sprites.draw(display.get_surface())
            self.clock.tick(self.option.tickrate)
            self.refresh()

    def refresh(self):
        display.flip()
        display.get_surface().fill(self.map.color())
        display.get_surface().blit(self.map.map, (0, 0))

    def createmap(self):
        self.map.make_map(self)
        self.addobject(self.map.player)

    def addobject(self, gameobject):
        self.gameobjects.append(gameobject)
