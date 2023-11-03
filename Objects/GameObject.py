from Objects.Transform import Transform


class GameObject:
    def __init__(self, position, name):
        self.transform = Transform(position, 0, 1)
        self.name = name

    @property
    def transform(self):
        return self._transform

    @transform.setter
    def transform(self, transform):
        if type(transform) != Transform:
            raise TypeError("Wrong type!")
        self._transform = transform

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = str(name)
