import pygame
from Objects import transform, collider


class GameObject(pygame.sprite.Sprite):

    def __init__(self, position, name="object", scale=1):
        super().__init__()
        self.transform = transform.Transform(position, 0, scale)
        self.collider = None
        self.name = name
        self.game = None
        self.collision = []

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

    def update(self, game):
        self.collision = []
        self.collider.colide([i for i in game.gameobjects if i != self and i.collider is not None])
        for c in self.collider.collision:
                self.on_collision(c)

    def on_collision(self, other):
        self.collision.append(other)

    def __str__(self):
        return self.name