from Systems.map import Map
from Systems.loader import Loader
import pygame


class Game:
    def __init__(self, root):
        self.root_dir = root
        self.map_manager = Map()
        self.loader = Loader(root)
        self.running = False

    def start_game(self):
        self.running = True
        pygame.display.set_mode((500, 500))
        while self.running:
            self.update()

    def update(self):
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                self.running = False
