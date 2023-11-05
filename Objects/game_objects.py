import pygame
from Objects import transform


class GameObject(pygame.sprite.Sprite):
    def __init__(self, position, name, scale=1):
        super().__init__()
        self.transform = transform.Transform(position, 0, scale)
        self.name = name
        self.game = None

    @property
    def transform(self):
        return self._transform

    @transform.setter
    def transform(self, trans):
        if type(trans) != transform.Transform:
            raise TypeError("Wrong type!")
        self._transform = trans

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
