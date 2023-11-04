import pygame
from Objects.Transform import Transform


class GameObject(pygame.sprite.Sprite):
    def __init__(self, position, name):
        super().__init__()
        self.transform = Transform(position, 0, 1)
        self.name = name
        self.game = None

    @property
    def transform(self):
        return self._transform

    @transform.setter
    def transform(self, transform):
        if type(transform) != Transform:
            raise TypeError("Wrong type!")
        self._transform = transform

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = str(name)

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        self._game = game

    def start(self, game):
        self.game = game

    def update(self):
        ...
