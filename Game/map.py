import pygame
import pytmx
import Game.Objects.Player.player as player
import Game.Objects.box as box
import Game.Objects.Gate.gate as gate
import dragon as dragon


class Map:
    TEST_MAP = "\\Map\\test..tmx"
    TEST2_MAP = "\\Map\\scaled..tmx"

    def __init__(self, game: object):
        self.tile_size = 18
        self.surfaces = []
        self.frontLayer = []
        self.backLayer = []
        self.color = "#000000"
        self.scene = None
        self.objects = []
        self.recipe = []
        self.game = game

    @property
    def color(self) -> tuple:
        if self._background_color:
            return self._background_color
        else:
            return 21, 21, 21

    @color.setter
    def color(self, color_hex: str) -> None:
        color = color_hex[1:]
        r = int(color[0:2], 16)
        g = int(color[2:4], 16)
        b = int(color[4:6], 16)
        self._background_color = (r, g, b)

    def load_map(self, path: str, spawn: int) -> None:
        self.scene = scene = pytmx.load_pygame(path)
        self.color = scene.background_color
        self.frontLayer = []
        self.backLayer = []
        self.objects = []
        self.recipe = []
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
                        if spawn > 0:
                            spawn -= 1
                        else:
                            self.recipe.append((lambda pos: player.Player((30, 36), pos), (obj.x, obj.y)))
                            break
                if layer.name == "Test":
                    for obj in layer:
                        self.recipe.append((lambda pos: dragon.Dragon(position=pos, direction=False), (obj.x, obj.y)))
                if layer.name == "Collision":
                    for obj in layer:
                        self.objects.append(box.Box((obj.width, obj.height), (obj.x, obj.y)))
                if layer.name == "Finish":
                    for obj in layer:
                        g = gate.Gate((obj.width, obj.height), (obj.x, obj.y), self.game, obj.path, obj.spawn)
                        self.objects.append(g)
                        self.objects.append(g.ui_icon)
                continue
            if layer.name[0:2] == "fr":
                self.frontLayer.append(surface)
            else:
                self.backLayer.append(surface)

    def get_objects(self):
        objects = self.objects.copy() + [ob[0](ob[1]) for ob in self.recipe]
        return objects
