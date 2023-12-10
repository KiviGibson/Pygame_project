import collision
import game
import gameobject


class SquereCollider(collision.Collision):

    def __init__(self, size: tuple, pos: tuple, parent: gameobject.GameObject) -> None:
        super().__init__(size, pos, parent)
        self.distance = size[0] / 2, size[1] / 2
        self.center = pos[0] + size[0] / 2, pos[1] + size[1] / 2
        self.size: tuple = size
        self.left = pos[0]
        self.right = pos[0] + size[0]
        self.top = pos[1]
        self.down = pos[1] + size[1]

    def check_if_colliding(self, other: gameobject.GameObject) -> bool:
        return self.parent.rect.colliderect(other)

    def check_direction(self, other: any) -> tuple[float | None, float | None, bool, bool]:
        up = abs(self.top - other.down)
        down = abs(self.down - other.top)
        right = abs(self.right - other.left)
        left = abs(self.left - other. right)
        if up < down and up < right and up < left:
            return None, other.down, False, True
        elif down < right and down < left:
            return None, other.top - self.size[1]+0.5, True, False
        elif right < left:
            return other.left - self.size[0]+1, None, True, False
        else:
            return other.right-1, None, False, True

    def collide_with(self, g: game.Game) -> list:
        col = [obj for obj in g.objects if obj is not self.parent and self.check_if_colliding(obj)]
        return col

    def update(self, x: float, y: float) -> None:
        self.left = x
        self.right = x + self.size[0]
        self.top = y
        self.down = y + self.size[1]
