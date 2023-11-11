from pygame import *
import pygame
from Game import options, map


class Game:
    def __init__(self, tickrate=60, size=(400, 500), name="Game Title", img=""):
        self.running = True
        self.option = options.Option(name, img, size, tickrate)
        self.clock = time.Clock()
        self.gameobjects = []
        self.userobjects = []
        self.events = []
        self.moving_sprites = pygame.sprite.Group()
        self.target = None
        option = self.option
        display.set_mode(option.size)
        display.set_caption(option.title)
        self.map = map.Map()
        if option.icon:
            icon = image.load(option.icon)
            display.set_icon(icon)

    def setup(self):
        self.createmap()

        for obj in self.map.colliders:
            self.addobject(obj)
        for entity in self.gameobjects:
            try:
                entity.start(self)
                self.moving_sprites.add(entity)
            except AttributeError:
                pass

    def start(self):
        self.setup()
        while self.running:
            self.getevents()
            for entity in self.gameobjects:
                try:
                    entity.update(self)
                except AttributeError:
                    pass
            self.clock.tick(self.option.tickrate)
            self.refresh()

    def getevents(self):
        self.events.clear()
        for e in event.get():
            if e.type == QUIT:
                self.running = False
            self.events.append(e)

    def refresh(self):
        display.flip()
        display.get_surface().fill(self.map.color())
        surface = pygame.surface.Surface((70 * 18, 70 * 18))
        surface.blits([(i, (0, 0)) for i in self.map.map[:4]])
        self.moving_sprites.draw(surface)
        surface.blits([(i, (0, 0)) for i in self.map.map[4:]])
        try:
            size = (display.get_surface().get_width(), display.get_surface().get_height())
            display.get_surface().blit(surface, (-self.target.transform.position[0]+size[0]/2, -self.target.transform.position[1]+size[1]/2))
        except:
            display.get_surface().blit(surface, (0, 0))

    def createmap(self):
        self.map.make_map(self)
        self.addobject(self.map.player)

    def addobject(self, gameobject):
        self.gameobjects.append(gameobject)
