import pygame
import pytmx
from Objects import player, tile


class Map:
    def __init__(self, map_path="./Game/Map/scaled..tmx"):
        self.tmxdata = pytmx.load_pygame(map_path)
        self.layer = []
        self.tilesize = 18
        self.map = None
        self.player = None
        self.colliders = []
        self.surfaces = []

    def color(self):
        if self.tmxdata.background_color:
            return self.tmxdata.background_color
        else:
            return 21, 21, 21

    def load(self, current_game):
        c = []

        surfaces = []
        for layer in self.tmxdata.layers:
            surface = pygame.Surface((self.tmxdata.width * 18, self.tmxdata.height * 18), pygame.SRCALPHA)
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, image in layer.tiles():
                    if image:
                        if layer.name == "player":
                            self.player = player.Player((x*18, y*18), current_game, scale=2, speed=3, skin="green")
                        else:
                            surface.blit(image.convert_alpha(), (x*18, y*18))
                            if layer.name == "playable":
                                c.append(tile.Tile((x*18, y*18)))
            surfaces.append(surface)
        self.surfaces = surfaces
        self.colliders = c

    def make_map(self, game):
        self.load(game)
        self.map = self.surfaces

    @property
    def map(self):
        return self._map

    @map.setter
    def map(self, m):
        self._map = m

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, p):
        self._player = p

    @property
    def colliders(self):
        return self._colliders

    @colliders.setter
    def colliders(self, colliders):
        self._colliders = colliders