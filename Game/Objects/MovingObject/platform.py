import definition
import Game.Objects.collisionobject as gm
import Game.loader as loader
import pygame


class Platform(gm.CollisionObject):
    def __init__(self, pos, segments, index, speed="0.2"):
        self.images = {
            "start": loader.Loader().load_image("/Images/platform/start", "png"),
            "mid": loader.Loader().load_image("/Images/platform/mid", "png"),
            "end": loader.Loader().load_image("/Images/platform/end", "png"),
            "single": loader.Loader().load_image("/Images/platform/single", "png")
        }
        self.funcs = {
            "move": lambda p: self.change_pos(p),
            "move_to": lambda p: self.change_pos_to(p)
        }
        super().__init__((18 * segments, 18), pos)
        self.create_platform(segments)
        self.postarget = [self.x, self.y]
        self.index = index
        self.speed = speed

    def create_platform(self, segments):
        self.image = pygame.surface.Surface((18 * segments, 18))
        if segments == 1:
            self.image.blit(self.images["single"], (0, 0))
        else:
            self.image.blit(self.images["start"], (0, 0))
            for i in range(segments-1):
                self.image.blit(self.images["mid"], ((i+1)*18, 0))
            self.image.blit(self.images["end"], ((segments-1)*18, 0))

    def change_pos(self, pos: str):
        self.postarget = list(pos.split(" "))
        self.postarget[0] = int(self.postarget[0]) * 18 + self.x
        self.postarget[1] = int(self.postarget[1]) * 18 + self.y

    def change_pos_to(self, pos: str):
        self.postarget = list(pos.split(" "))
        self.postarget[0] = int(self.postarget[0])
        self.postarget[1] = int(self.postarget[1])

    def update(self, game):
        self.move()
        self.collider.update(self.x, self.y)

    def on_collision(self, other):
        ...

    def move(self) -> None:
        self.y = definition.lerp(self.y, self.postarget[1], self.speed)
        self.x = definition.lerp(self.x, self.postarget[0], self.speed)
        self.x = round(self.x, 1)
        self.y = round(self.y, 1)
        super().move(0, 0)
