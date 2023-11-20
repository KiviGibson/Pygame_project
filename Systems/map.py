import pygame
import pytmx


class Map:
    def __init__(self):
        self.scene = None
        self.tilesize = 18
        self.surfaces = []

    def color(self) -> tuple:
        if self.scene.background_color:
            return self.scene.background_color
        else:
            return 21, 21, 21

    def load_map(self, path: str) -> None:
        scene = pytmx.load_pygame(path)
        self.surfaces = []
        for layer in self.scene.layers:
            surface = pygame.Surface((self.scene.width * 18, self.scene.height * 18), pygame.SRCALPHA)
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    if image:
                        ...
            if isinstance(layer, pytmx.TiledObjectGroup):
                ...
            self.surfaces.append(surface)
