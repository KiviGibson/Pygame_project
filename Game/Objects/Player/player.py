import pygame

from Game.Objects import gameobject


class Player(gameobject.GameObject):
    speed = 3

    def __init__(self):
        super().__init__((50, 50), (200, 200), (100, 50, 230))
        self.mov_x = 0

    def update(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.press_button(event.key)
            elif event.type == pygame.KEYUP:
                self.release_button(event.key)
        self.move()

    def press_button(self, button):
        match button:
            case pygame.K_d:
                self.mov_x += 1
            case pygame.K_a:
                self.mov_x -= 1

    def release_button(self, button):
        match button:
            case pygame.K_d:
                self.mov_x -= 1
            case pygame.K_a:
                self.mov_x += 1

    def move(self):
        self.rect.x += self.mov_x * Player.speed
