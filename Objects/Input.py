import pygame


class Input:
    def __init__(self, game):
        self.x_axis = 0
        self.y_axis = 0
        self.shift = 0
        self.jump = 0
        self.game = game
        self.joystick = None
        pygame.joystick.init()
        if pygame.joystick.get_init():
            try:
                self.joystick = pygame.joystick.Joystick(0)
                print(self.joystick.get_name() + " was connected successfully!")
            except:
                pass

    def events(self):
        if self.joystick is not None:
            self.x_axis = int(self.joystick.get_axis(0)*1.2)
            self.x_axis += self.joystick.get_hat(0)[0]
            self.shift = self.joystick.get_button(5)
            self.jump = self.joystick.get_button(2)
        else:
            for event in self.game.events:
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_a:
                            self.x_axis = self.x_axis - 1
                        case pygame.K_d:
                            self.x_axis = self.x_axis + 1
                        case pygame.K_LSHIFT:
                            self.shift = 1
                        case pygame.K_SPACE:
                            self.jump = 1
                        case _:
                            print("none pressed")
                elif event.type == pygame.KEYUP:
                    match event.key:
                        case pygame.K_a: 
                            self.x_axis = self.x_axis + 1
                        case pygame.K_d:
                            self.x_axis = self.x_axis - 1
                        case pygame.K_LSHIFT:
                            self.shift = 0
                        case pygame.K_SPACE:
                            self.jump = 0
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
