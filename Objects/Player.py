from Objects import game_objects, input, collider
from Game import loader
import pygame


class Player(game_objects.GameObject):
    def __init__(self, position, game, speed=3, scale=1, skin="green"):
        super().__init__(position, "Player", scale)
        self.loader = loader.Loader()
        self.animations = {
            "idle": self.loader.loadimageArray(f"/{skin}/idle", "png"),
            "walk": self.loader.loadimageArray(f"/{skin}/walk", "png"),
            "damage": self.loader.loadimageArray(f"/{skin}/damage", "png"),
            "run": self.loader.loadimageArray(f"/{skin}/run", "png"),
            "idle_run": self.loader.loadimageArray(f"/{skin}/idle_run", "png"),
        }
        self.input = input.Input(game)
        self.speed = speed
        self.image = self.animations["idle"][0]
        self.rect = self.animations["idle"][0].get_rect()
        self.rect.topleft = self.transform.position
        self.currentsprite = 0
        self.state = "idle"
        self.facing = 0
        self.acc = 1
        self.y = 0
        self.left = 1
        self.right = 1
        size = 18*self.transform.scale
        self.collider = collider.Collider(self.transform.position[0], self.transform.position[1], size-3, size)
        self.onground = True

    def __str__(self):
        return super().__str__()

    def conditional_stop(self, x):
        if self.right == 0 and x <= 0:
            x = 0
        if self.left == 0 and x >= 0:
            x = 0
        return x

    def update(self, game):
        pos = self.transform.position
        self.collider.update(pos[0], pos[1])
        super().update(self.game)
        self.input.events()
        self.check_collision()
        x = self.conditional_stop(self.input.x_axis)
        self.setstate(x)
        self.changepos(x)
        self.animate()
        self.rect.topleft = self.transform.position
    
    def start(self, game):
        super().start(game)

    def check_collision(self):
        self.left = 1
        self.right = 1
        for i in self.collision:
            if i["dir"] == "left":
                self.left = 0
            elif i["dir"] == "right":
                self.right = 0

    def setstate(self, x):
        if x != 0:
            self.facing = int(0.5 + (-x))
        if self.input.shift == 1 or (self.state == "run" and x != 0):
            if x != 0:
                self.state = "run"
            else:
                self.state = "idle_run"
        else:
            if x != 0:
                self.state = "walk"
            else:
                self.state = "idle"

    def animate(self):
        self.currentsprite += 0.20
        self.currentsprite %= len(self.animations[self.state])
        self.image = self.animations[self.state][int(self.currentsprite)]
        self.image = pygame.transform.flip(self.image, bool(self.facing), 0)
        scale = [self.image.get_width()*self.transform.scale, self.image.get_height()*self.transform.scale]
        self.image = pygame.transform.scale(self.image, scale)


    def changepos(self, x):
        speed = self.speed
        if not self.collider.onground:
            self.y += self.gravity()
        else:
            self.y = 0
        if self.state == "run":
            speed *= self.acc
            self.acc += 0.07
            self.acc = min(self.acc, 5)
        else:
            self.acc = 1
        new = (x * speed, self.y)
        self.transform.move(new)


    @staticmethod
    def gravity():
        return 0.25
