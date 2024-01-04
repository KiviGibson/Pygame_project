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
        return self.parent.rect.colliderect(other)

    def check_if_trigger(self, obj: gameobject):
        try:
            return obj.collider.trigger
        except AttributeError:
            return False

    def check_direction(self, other: any) -> tuple[float | None, float | None, bool, bool]:
        up = abs(self.top - other.down)
        down = abs(self.down - other.top)
        right = abs(self.right - other.left)
        left = abs(self.left - other. right)
        if up < down and up < right and up < left:
            return None, other.down, False, True
        elif down < right and down < left:
            return None, other.top - self.size[1] + 0.5, True, False
        elif right < left:
            return other.left - self.size[0] + 1, None, True, False
        else:
            return other.right - 1, None, False, True

    def have_collider(self, other):
        try:
            if other.collider:
                return True
        except AttributeError:
            return False

    def collide_with(self, g: object) -> list:
        c = [obj for obj in g.objects if self.have_collider(obj)]
        col = [obj for obj in c if obj is not self.parent and self.check_if_colliding(obj) and not self.check_if_trigger(obj)]
        trigger = [obj for obj in c if obj is not self.parent and self.check_if_colliding(obj) and self.check_if_trigger(obj)]
        for c in col:
            try:
                c.collider.on_collision(self)
            except AttributeError:
                pass
        for t in trigger:
            t.collider.on_collision(self)
        return col

    def update(self, x: float, y: float) -> None:
        self.left = x
        self.right = x + self.size[0]
        self.top = y
        self.down = y + self.size[1]
