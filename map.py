import pygame
import pytmx


class Map:
    def __init__(self, map_path="./Game/Map/scaled..tmx"):
        self.tmxdata = pytmx.load_pygame(map_path)
        self.tilesize = 18
        self.surfaces = []

    def color(self):
        if self.tmxdata.background_color:
            return self.tmxdata.background_color
        else:
            return 21, 21, 21

    def load(self, current_game):
        self.surfaces = []
        for layer in self.tmxdata.layers:
            surface = pygame.Surface((self.tmxdata.width * 18, self.tmxdata.height * 18), pygame.SRCALPHA)
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    if image:
                        ...
            if isinstance(layer, pytmx.TiledObjectGroup):
                ...
            self.surfaces.append(surface)

    def make_map(self, game):
        self.load(game)
