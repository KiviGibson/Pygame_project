import pygame
from pygame import sprite, Surface
import Game.game as game


class GameObject(sprite.Sprite):
    SPEED = 4

    def __init__(self,
                 size=(50, 50),
                 position=(200, 200),
                 color=(0, 0, 0),
                 img: Surface | None = None,
                 render=True,
                 visible=True,
                 simulate=False):

        super().__init__()
        self.image = Surface(size, pygame.SRCALPHA)

        try:
            self.image.blit(img, (0, 0))
        except TypeError:
            self.image.fill(color)
        self.render = render
        self.visible = visible
        self.x, self.y = position
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y

        self.simulate = simulate
        self.mov_x: float = 0
        self.mov_y: float = 0

    def calculate_movement(self) -> float:
        x = self.mov_x * GameObject.SPEED
        return x

    @staticmethod
    def gravity(y, on_ground) -> float:
        if on_ground:
            return min(y, 0)
        return y + game.Game.GRAVITY

    def on_collision(self, other):
        ...

    def on_trigger(self,other):
        ...

    def move(self, x, y) -> None:
        self.x += x
        self.y += y
        self.change_sprite_pos()

    def change_sprite_pos(self) -> None:
        self.rect.x = self.x
        self.rect.y = self.y

