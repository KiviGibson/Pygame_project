import Game.Objects.gameobject as gameobject
import Game.Objects.Components.Colliders.squere_collider as squere_collider


class Box(gameobject.GameObject):
    def __init__(self, size=(50, 50), position=(200, 200), color=(30, 10, 230, 255)):
        super().__init__(size, position, color, render=False)
        self.collider = squere_collider.SquereCollider(size, position, self)
