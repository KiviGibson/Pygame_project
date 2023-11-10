from Objects import collider


class Tile:
    def __init__(self, pos):
        self.collider = collider.Collider(pos[0], pos[1], 18, 18)

