import pygame
import pytmx
import player
import box


class Map:
    TEST_MAP = "\\Map\\test..tmx"
    TEST2_MAP = "\\Map\\scaled..tmx"

    def __init__(self):
        self.tile_size = 18
        self.surfaces = []
        self.frontLayer = []
        self.backLayer = []
        self.background_color = None
        self.scene = None
        self.objects = []

    def color(self) -> tuple:
        if self.background_color:
            return self.background_color
        else:
            return 21, 21, 21

    def load_map(self, path: str) -> None:
        scene = pytmx.load_pygame(path)
        self.background_color = scene.background_color
        self.frontLayer = []
        self.backLayer = []
        self.objects = []
        for layer in scene.layers:
            size = (scene.width * self.tile_size, scene.height * self.tile_size)
            surface = pygame.Surface(size, pygame.SRCALPHA)
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    if image:
                        surface.blit(image, (x * 18, y * 18))
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == "Player":
                    for obj in layer:
                        self.objects.append(player.Player((18, 18), (obj.x, obj.y)))
                if layer.name == "Collision":
                    for obj in layer:
                        self.objects.append(box.Box((obj.width, obj.height), (obj.x, obj.y)))
                continue
            if layer.name[0:2] == "fr":
                self.frontLayer.append(surface)
            else:
                self.backLayer.append(surface)
