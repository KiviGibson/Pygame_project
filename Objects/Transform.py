class Transform:
    def __init__(self, position, rotation, scale):
        self.position = position
        self.rotation = rotation
        self.scale = scale

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = [position[0], position[1]]

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, degree):
        self._rotation = degree % 361

    @property
    def scale(self):
        return self._scale

    @scale.setter
    def scale(self, scale):
        self._scale = scale

    def move(self, position):
        pos = self.position
        new = (pos[0]+position[0], pos[1]+position[1])
        self.position = new