import Game.Objects.collision as collision
import Game.Objects.gameobject as gameobject


class SquereCollider(collision.Collision):
    def __init__(self, size: tuple, pos: tuple, parent: gameobject.GameObject, trigger=False) -> None:
        super().__init__(size, pos, parent, trigger=trigger)
        self.distance = size[0] / 2, size[1] / 2
        self.center = pos[0] + size[0] / 2, pos[1] + size[1] / 2
        self.size: tuple = size
        self.left = pos[0]
        self.right = pos[0] + size[0]
        self.top = pos[1]
        self.down = pos[1] + size[1]

    def check_if_colliding(self, other: gameobject.GameObject) -> bool:
        return self.parent.rect.colliderect(other) and other is not self.parent

    @staticmethod
    def check_if_trigger(obj: gameobject):
        try:
            return obj.collider.trigger
        except AttributeError:
            return False

    def have_collider(self, other):
        try:
            if other.collider:
                return self.check_if_colliding(other)
            else:
                return False
        except AttributeError:
            return False

    def check_collision(self, objects: gameobject) -> list:
        collider = []
        for c in filter(self.have_collider, objects):
                collider.append((c, self.check_if_trigger(c)))
        return collider

    def collide_with(self, g: object) -> list[tuple[object, bool]]:
        col, trigger = self.check_collision(g.objects)
        for c in col:
            c.collider.on_collision(self)
        for t in trigger:
            t.collider.on_collision(self)
        return col

    def check_side(self, other: object) -> int:
        under = abs(self.top - other.down)
        ontop = abs(self.down - other.top)
        onleft = abs(self.left - other.right)
        onright = abs(self.right - other.left)
        if under < ontop and under < onright and under < onleft:
            return self.SIDES["down"]
        elif ontop < onright and ontop < onleft:
            return self.SIDES["top"]
        elif onright < onleft:
            return self.SIDES["left"]
        else:
            return self.SIDES["right"]

    def update(self, x: float, y: float) -> None:
        self.left = x
        self.right = x + self.size[0]
        self.top = y
        self.down = y + self.size[1]
