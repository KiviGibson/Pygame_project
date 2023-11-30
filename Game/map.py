import pygame
import pytmx


class Map:
    TEST_MAP = "\\Map\\test..tmx"

    def __init__(self):
        self.tile_size = 18
        self.surfaces = []
        self.frontLayer = []
        self.backLayer = []
        self.background_color = None
        self.scene = None

    def color(self) -> tuple:
        if self.background_color:
            return self.background_color
        else:
            return 21, 21, 21

    def load_map(self, path: str) -> None:
        scene = pytmx.load_pygame(path)
        self.background_color = scene.background_color
        self.frontLayer = []
        for layer in scene.layers:
            size = (scene.width * self.tile_size, scene.height * self.tile_size)
            surface = pygame.Surface(size, pygame.SRCALPHA)
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    if image:
                        surface.blit(image, (x * 18, y * 18))
            if isinstance(layer, pytmx.TiledObjectGroup):
                ...
                continue
            self.frontLayer.append(surface)
