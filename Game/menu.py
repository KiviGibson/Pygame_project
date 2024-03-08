import pygame
import definition as df

class Menu:
    def __init__(self):
        self.screen = pygame.surface.Surface((1260, 1260))
        self.screen.fill((21, 21, 21))
        self.font = pygame.font.Font(f"{df.ROOT_PATH}/Images/AtariClassic-gry3.ttf", 18)
        self.pulse = 200
        self.dir = -0.5

    def update(self):
        self.pulse -= self.dir
        if self.pulse <= 50 or self.pulse >= 255:
            self.dir = -self.dir
        self.render()

    def render(self):
        screen = pygame.display.get_surface()
        screen_size = pygame.display.get_window_size()
        center = screen_size[0]//2, screen_size[1]//2
        screen.blit(self.screen, (0, 0))
        text = self.font.render("Press anything to start!", False, (self.pulse, self.pulse, self.pulse))
        screen.blit(text, (center[0] - text.get_width()//2, screen_size[1] - 60 - text.get_height()//2))
        pygame.display.flip()
