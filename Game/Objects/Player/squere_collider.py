import collision
import game
import pygame


class SquereCollider(collision.Collision):

    def __init__(self, size: tuple, pos: tuple, parent: pygame.sprite.Sprite):
        super().__init__(size, pos, parent)
        self.distance = size[0] / 2, size[1] / 2
        self.center = pos[0] + size[0] / 2, pos[1] + size[1] / 2

    def check_if_colliding(self, other: pygame.sprite.Sprite) -> bool:
        return self.parent.rect.colliderect(other)

    def change_collider_pos(self, x: float, y: float) -> None:
        self.center = x + self.distance[0] / 2, y + self.distance[1] / 2

    def check_direction(self, other: collision.Collision):
        ...

    def collide_with(self, g: game.Game) -> list:
        col = [obj for obj in g.objects if obj is not self.parent and self.check_if_colliding(obj)]
        return col
