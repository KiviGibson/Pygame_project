import pygame
import pytmx


class Map:
    def __init__(self):
        self.scene = None
        self.tile_size = 18
        self.surfaces = []

    def color(self) -> tuple:
        if self.scene.background_color:
            return self.scene.background_color
        else:
            return 21, 21, 21

    def load_map(self, path: str) -> None:
        self.scene = pytmx.load_pygame(path)
        self.surfaces = []
        for layer in self.scene.layers:
            size = (self.scene.width * self.tile_size, self.scene.height * self.tile_size)
            surface = pygame.Surface(size, pygame.SRCALPHA)
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    if image:
                        ...
            if isinstance(layer, pytmx.TiledObjectGroup):
                ...
            self.surfaces.append(surface)
