from Systems.map import Map
from Systems.loader import Loader
class Game:
    def __init__(self):
        self.map_manager = Map()
        img = Loader.load_image("/div", "png")
