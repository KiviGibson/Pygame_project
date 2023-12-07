import game
import pygame


class Collision:

    def __init__(self, size: tuple, pos: tuple, parent: pygame.sprite.Sprite):
        self.parent = parent
        self.y: float = pos[0]
        self.x: float = pos[1]
        self.size: tuple = size
        self.distance = []
        self.center = [0, 0]

    def change_collider_pos(self, x: float, y: float) -> None:
        """
        Change position of collider in space to passed value
        """

    def collide_with(self, g: game.Game) -> list:
        """
        return all colliding objects
        """
        return list()
