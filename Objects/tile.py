from Objects import collider


class Tile:
    def __init__(self, pos, size):
        self.collider = collider.Collider(pos[0], pos[1], size[0], size[1])

