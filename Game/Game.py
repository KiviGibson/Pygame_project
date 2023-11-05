from pygame import *
import pygame
from Game import options


class Game:
    def __init__(self, tickrate=60, size=(400, 500), name="Game Title", img=""):
        init()
        self.running = True
        self.option = options.Option(name, img, size, tickrate)
        self.clock = time.Clock()
        self.gameobjects = []

        self.userobjects = []
        self.events = []

        option = self.option
        display.set_mode(option.size)
        display.set_caption(option.title)

        if option.icon:
            icon = image.load(option.icon)
            display.set_icon(icon)

    def start(self):
        moving_sprites = pygame.sprite.Group()
        for entity in self.gameobjects:
            entity.start(self)
            moving_sprites.add(entity)

        while self.running:
            self.events.clear()
            for e in event.get():
                if e.type == QUIT:
                    self.running = False
                self.events.append(e)
            for entity in self.gameobjects:
                entity.update()
            moving_sprites.draw(display.get_surface())
            self.clock.tick(self.option.tickrate)
            self.refresh()

    def refresh(self):
        display.flip()
        display.get_surface().fill(self.option.color)

    def addobject(self, gameobject):
        self.gameobjects.append(gameobject)
