import pygame

from Game.Objects import gameobject
import Game.game as game
from squere_collider import SquereCollider


class Player(gameobject.GameObject):
    speed = 3

    def __init__(self, size: tuple, position: tuple):
        super().__init__(size, position, (100, 50, 230))
        self.mov_x = 0
        self.mov_y = 0
        self.collider = SquereCollider((18, 18), (self.x, self.y), self)

    def update(self, g):
        for event in g.events:
            if event.type == pygame.KEYDOWN:
                self.press_button(event.key)
            elif event.type == pygame.KEYUP:
                self.release_button(event.key)
        self.move(g)

    def press_button(self, button):
        match button:
            case pygame.K_d:
                self.mov_x += 1
            case pygame.K_a:
                self.mov_x -= 1
            case pygame.K_s:
                self.mov_y += 1

    def release_button(self, button):
        match button:
            case pygame.K_d:
                self.mov_x -= 1
            case pygame.K_a:
                self.mov_x += 1
            case pygame.K_s:
                self.mov_y -= 1

    def move(self, g):
        self.mov_y += game.Game.GRAVITY
        if len(self.collider.collide_with(g)) > 0:
            self.mov_y = 0
            self.y = int(self.y)
        self.x += self.mov_x * Player.speed
        self.y += self.mov_y
        self.change_sprite_pos()
        self.collider.change_collider_pos(self.x, self.y)

    def change_sprite_pos(self):
        self.rect.x = self.x
        self.rect.y = self.y
