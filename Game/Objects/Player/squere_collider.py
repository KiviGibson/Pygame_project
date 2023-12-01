import collision
import game


class SquereCollider(collision.Collision):

    def __init__(self, size: tuple, pos: tuple, parent: object):
        super().__init__(size, pos, parent)
        self.distance = size[0] / 2, size[1] / 2
        self.center = pos[0] + size[0] / 2, pos[1] + size[1] / 2

    def check_if_collideing(self, other: collision.Collision) -> bool:
        x_dist = self.distance[0] + other.distance[0]
        y_dist = self.distance[1] + other.distance[1]
        if x_dist <= abs(self.center[0] - other.center[0]):
            if y_dist <= abs(self.center[1] - other.center[0]):
                return True
        return False

    def change_collider_pos(self, x: float, y: float) -> None:
        super().change_collider_pos(x, y)
        self.center = x + self.distance[0] / 2, x + self.distance[1] / 2

    def collide_with(self, g: game.Game) -> list:
        col = [obj for obj in g.objects if obj is not self.parent and self.check_if_collideing(obj.collider)]
        print(col)
        return col
