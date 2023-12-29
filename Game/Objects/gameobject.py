import pygame
from pygame import sprite, Surface


class GameObject(sprite.Sprite):

    def __init__(self, size=(50, 50), position=(200, 200), color=(0, 0, 0), img: Surface | None = None, render=True):
        super().__init__()
        self.image = Surface(size, pygame.SRCALPHA)
        try:
            self.image.blit(img, (0, 0))
        except TypeError:
            self.image.fill(color)
        self.render = render
        self.x, self.y = position
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

    def on_collision(self, other):
        pass
