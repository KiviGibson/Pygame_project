import pygame


class Input:
    def __init__(self, game):
        self.x_axis = 0
        self.y_axis = 0
        self.shift = 0
        self.game = game

    def events(self):
        for event in self.game.events:
            if event.type == pygame.KEYDOWN:
                match event.key:
                    case pygame.K_w:
                        self.y_axis = self.y_axis - 1
                    case pygame.K_s:
                        self.y_axis = self.y_axis + 1
                    case pygame.K_a:
                        self.x_axis = self.x_axis - 1
                    case pygame.K_d:
                        self.x_axis = self.x_axis + 1
                    case pygame.K_LSHIFT:
                        self.shift = 1
                    case _:
                        print("none pressed")
            elif event.type == pygame.KEYUP:
                match event.key:
                    case pygame.K_w:
                        self.y_axis = self.y_axis + 1
                    case pygame.K_s:
                        self.y_axis = self.y_axis - 1
                    case pygame.K_a:
                        self.x_axis = self.x_axis + 1
                    case pygame.K_d:
                        self.x_axis = self.x_axis - 1
                    case pygame.K_LSHIFT:
                        self.shift = 0
                    case _:
                        print("none unpressed")

    @property
    def x_axis(self):
        return self._x_axis

    @x_axis.setter
    def x_axis(self, direction):
        self._x_axis = direction

    @property
    def y_axis(self):
        return self._y_axis

    @y_axis.setter
    def y_axis(self, direction):
        self._y_axis = direction
