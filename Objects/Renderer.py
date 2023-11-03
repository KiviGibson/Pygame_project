from pygame import *


class Renderer:
    def __init__(self, scale=(1, 1), imagepath="", color=(255, 255, 255)):
        self.width = scale[0]
        self.height = scale[1]
        self.color = color
        try:
            self.img = image.load(imagepath)
        except FileNotFoundError:
            self.img = None

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, width: float):
        self._width = float(width)

    @height.setter
    def height(self, height: float):
        self._height = float(height)

    def draw(self, x, y):
        if not self.img:
            draw.rect(display.get_surface(), self.color, [x, y, 32 * self.width, 32 * self.height])
