from pygame import sprite, Surface


class GameObject(sprite.Sprite):

    def __init__(self, size=(50, 50), position=(200, 200), color="white"):
        super().__init__()
        self.image = Surface(size)
        self.image.fill(color)
        self.x, self.y = position
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
