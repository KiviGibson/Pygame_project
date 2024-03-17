import pygame
import definition as df
import Game.Objects.gameobject as gm


class Text(gm.GameObject):
    def __init__(self, string: str, position):

        self.font = pygame.font.Font(df.ROOT_PATH+"/Images/AtariClassic-gry3.ttf", 11)
        print(string)
        self.text = self.font.render(string, 0, (255, 255, 255))
        super().__init__((self.text.get_width(), self.text.get_height()),
                         (position[0] - self.text.get_width()//2, position[1]),
                         img=self.text)
