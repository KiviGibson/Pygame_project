from pygame import sprite, Surface


class GameObject(sprite.Sprite):

    def __init__(self, size=(50, 50), position=(200, 200), color="white"):
        super().__init__()
        self.image = Surface(size)
        self.image.fill(color)

        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def __repr__(self) -> sprite.Sprite:
        return self
