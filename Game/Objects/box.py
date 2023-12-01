import gameobject
import squere_collider


class Box(gameobject.GameObject):
    def __init__(self, size=(50, 50), position=(200, 200), color=(30, 10, 230)):
        super().__init__( size, position, color)
        self.collider = squere_collider.SquereCollider(size, position, self)
