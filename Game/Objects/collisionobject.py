import Game.Objects.Components.Colliders.squere_collider as squere
import Game.Objects.gameobject as gm
from pygame import Surface


class CollisionObject(gm.GameObject):

    def __init__(self,
                 size=(50, 50),
                 position=(200, 200),
                 color=(0, 0, 0),
                 img: Surface | None = None,
                 render=True,
                 visible=True,
                 simulate=False):
        super().__init__(size, position, color, img, render, visible, simulate)
        self.collider: squere.SquereCollider = squere.SquereCollider(size, (self.x, self.y), self)
        self.on_ground = True
        self.check_on_ground = self.on_ground

    def sim(self, g: any):
        self.on_ground = False
        for collision in self.collider.check_collision(g.objects):
            if collision[1] is False:
                self.on_collision(collision[0])
                collision[0].on_collision(self)
            else:
                self.on_trigger(collision[0])
                collision[0].on_trigger(self)
        self.check_on_ground = self.on_ground

    def on_trigger(self, other):
        ...

    def on_collision(self, other):
        side = self.collider.check_side(other.collider)
        if side == self.collider.SIDES["top"]:
            self.on_ground = True
            self.y = other.collider.top - self.rect.height + 0.5
        elif side == self.collider.SIDES["down"]:
            if not self.check_on_ground:
                self.y = other.collider.down
                self.mov_y = 1
        elif side == self.collider.SIDES["left"]:
            self.x = other.collider.left - self.rect.width + 0.5
        elif side == self.collider.SIDES["right"]:
            self.x = other.collider.right
