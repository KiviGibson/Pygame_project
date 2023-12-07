import pygame

from Game.Objects import gameobject
import Game.game as game
from squere_collider import SquereCollider


class Player(gameobject.GameObject):
    SPEED = 2

    def __init__(self, size: tuple, position: tuple) -> None:
        super().__init__(size, position, (100, 50, 230))
        self.mov_x = 0
        self.mov_y = 0
        self.collider = SquereCollider((18, 18), (self.x, self.y), self)

    def update(self, g) -> None:
        for event in g.events:
            if event.type == pygame.KEYDOWN:
                self.press_button(event.key)
            elif event.type == pygame.KEYUP:
                self.release_button(event.key)
        self.move(g)
        self.collider.update(self.x, self.y)

    def press_button(self, button: int) -> None:
        match button:
            case pygame.K_d:
                self.mov_x += 1
            case pygame.K_a:
                self.mov_x -= 1
            case pygame.K_SPACE:
                self.jump()

    def release_button(self, button: int) -> None:
        match button:
            case pygame.K_d:
                self.mov_x -= 1
            case pygame.K_a:
                self.mov_x += 1

    def move(self, g) -> None:
        self.mov_y += game.Game.GRAVITY
        for obj in self.collider.collide_with(g):
            x, y, on_ground, hit_celling = self.collider.check_direction(obj.collider)
            try:
                self.x = float(x)
            except TypeError:
                self.y = float(y)
                if on_ground:
                    self.mov_y = min(self.mov_y, 0)
                if hit_celling:
                    self.mov_y = max(self.mov_y, 0)
        self.x += self.mov_x * Player.SPEED
        self.y += self.mov_y
        self.change_sprite_pos()

    def jump(self) -> None:
        self.mov_y = -5.0

    def change_sprite_pos(self) -> None:
        self.rect.x = self.x
        self.rect.y = self.y
