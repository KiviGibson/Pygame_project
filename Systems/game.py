from Systems.map import Map
from Systems.loader import Loader


class Game:
    def __init__(self, root):
        self.root_dir = root
        self.map_manager = Map()
        self.loader = Loader(root)
        self.running = False

    def start_game(self):
        self.running = True
        while self.running:
            ...

    def update(self):
        ...