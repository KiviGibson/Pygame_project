import pygame
import pytmx
import Game.Objects.Player.player as player
import Game.Objects.Box.box as box
import Game.Objects.Gate.gate as gate
import Game.Objects.Enemies.RedDragon.dragon as dragon
import Game.Objects.Enemies.Jumper.jumper as jumper
import Game.Objects.Enemies.Walkie.walkie as walkie
import Game.Objects.Coins.coins as coin
import Game.Objects.Preasureplate.preasureplate as preasure_plate
import Game.Objects.MovingObject.platform as platform
import Game.Objects.Killzone.killzone as killzone


class Map:

    def __init__(self, game: object):
        self.maps = {
            "test": "\\Map\\test..tmx",
            "forest_1": "\\Map\\forest_1..tmx",
            "forest_2": "\\Map\\forest_2..tmx"
        }
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
        spawn = int(spawn)
        for layer in scene.layers:
            size = (scene.width * self.tile_size, scene.height * self.tile_size)
            surface = pygame.Surface(size, pygame.SRCALPHA)
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    if image:
                        surface.blit(image, (x * 18, y * 18))
            if isinstance(layer, pytmx.TiledObjectGroup):
                if layer.name == "player":
                    for obj in layer:
                        if spawn > 0:
                            spawn -= 1
                        else:
                            self.recipe.append((lambda pos: player.Player((30, 36), pos), (obj.x, obj.y)))
                            break
                if layer.name == "walkie":
                    for obj in layer:
                        self.recipe.append((lambda pos: walkie.Walkie(position=pos, direction=False), (obj.x, obj.y)))
                elif layer.name == "jumper":
                    for obj in layer:
                        self.recipe.append((lambda pos: jumper.Jumper(position=pos, direction=False), (obj.x, obj.y)))
                elif layer.name == "dragon":
                    for obj in layer:
                        self.recipe.append((lambda pos: dragon.Dragon(position=pos, direction=False), (obj.x, obj.y)))
                elif layer.name == "collision":
                    for obj in layer:
                        self.objects.append(box.Box((obj.width, obj.height), (obj.x, obj.y)))
                elif layer.name == "finish":
                    for obj in layer:
                        g = gate.Gate((obj.width, obj.height), (obj.x, obj.y), self.game, obj.path, obj.spawn)
                        self.objects.append(g)
                elif layer.name == "preasure_plate":
                    for obj in layer:
                        self.recipe.append((lambda params: preasure_plate.PreasurePlate(params[0], params[1], params[2], params[3], params[4]), ((18, 18), (obj.x, obj.y), obj.targets, obj.methods, obj.params)))
                elif layer.name == "moving_object":
                    for obj in layer:
                        self.recipe.append((lambda params: platform.Platform(params[0], params[1], params[2]), ((obj.x, obj.y), obj.segments, obj.index)))
                elif layer.name == "coins":
                    for obj in layer:
                        self.recipe.append((lambda pos: coin.Coin(pos), (obj.x, obj.y)))
                elif layer.name == "killzone":
                    for obj in layer:
                        self.objects.append(killzone.Killzone((obj.width, obj.height), (obj.x, obj.y)))
                continue
            if layer.name[0:2] == "fr":
                self.frontLayer.append(surface)
            else:
                self.backLayer.append(surface)

    def get_objects(self):
        objects = self.objects.copy() + [ob[0](ob[1]) for ob in self.recipe]
        return objects
