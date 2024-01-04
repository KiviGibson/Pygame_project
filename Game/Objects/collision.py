import Game.Objects.gameobject as gameobject


class Collision:

    def __init__(self, size: tuple, pos: tuple, parent: gameobject.GameObject, trigger=False):
        self.parent = parent
        self.y: float = pos[0]
        self.x: float = pos[1]
        self.size: tuple = size
        self.distance = []
        self.center = [0, 0]
        self.trigger = trigger

    def change_collider_pos(self, x: float, y: float) -> None:
        """
        Change position of collider in space to passed value
        """

    def collide_with(self, g: object) -> list:
        """
        return all colliding objects
        """
        return list()

    def on_collision(self, other) -> None:
        self.parent.on_collision(other)
