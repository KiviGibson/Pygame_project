import Game.Objects.collisionobject as gm
import Game.loader as loader
import pygame


class Platform(gm.CollisionObject):
    def __init__(self, pos, segments, side):
        super().__init__(pos)
        self.images = {
            "start": loader.Loader().load_image("/Images/platform/start", "png"),
            "mid": loader.Loader().load_image("/Images/platform/mid", "png"),
            "end": loader.Loader().load_image("/Images/platform/end", "png"),
            "single": loader.Loader().load_image("/Images/platform/single", "png")
        }
        self.create_platform(segments, side)

    def create_platform(self, segments, side):
        self.image = pygame.surface.Surface((18 * segments, 18))
        if segments == 1:
            self.image.blit(self.images["single"], (0, 0))
        else:
            self.image.blit(self.images["start"], (0, 0))
            for i in range(segments-1):
                self.image.blit(self.images["mid"], ((i+1)*18, 0))
            self.image.blit(self.images["end"], ((segments-1)*18, 0))
