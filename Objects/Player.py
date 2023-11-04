from Objects.GameObject import GameObject
from Objects.Input import Input
from Game.Loader import Loader
import pygame

class Player(GameObject):
    def __init__(self, position, sprite, game, speed=5):
        super().__init__(position, "Player")
        self.loader = Loader("../Animations")
        self.animations = {
            "idle": self.loader.loadimageArray("/Player/idle", "png"),
            "walk": self.loader.loadimageArray("/Player/walk", "png")
        }
        self.input = Input(game)
        self.speed = speed
        self.image = self.animations["idle"][0]
        self.rect = self.animations["idle"][0].get_rect()
        self.rect.topleft = self.transform.position
        self.currentsprite = 0
        self.state = "idle"
        self.facing = 0

    def update(self):
        self.input.events()
        speed = self.speed
        move = (self.input.x_axis * speed, self.input.y_axis * speed)
        self.transform.move(move)
        if self.input.x_axis != 0:
            self.facing = int(0.5+(-self.input.x_axis))
        self.animate(move)
        self.rect.topleft = self.transform.position
    def animate(self, move):
        if move[0] != 0 or move[1] != 0:
            if self.state == "idle":
                self.currentsprite = 0
                self.state = "walk"
        else:
            if self.state == "walk":
                self.currentsprite = 0
                self.state = "idle"

        self.currentsprite += 0.25
        self.currentsprite %= len(self.animations[self.state])
        self.image = self.animations[self.state][int(self.currentsprite)]
        self.image = pygame.transform.flip(self.image, self.facing, 0)
