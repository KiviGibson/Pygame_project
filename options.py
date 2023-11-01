import pygame

class Option:
    def __init__(self, title, icon, size):
        self.title = title
        self.icon = icon
        self.size = size

    @property
    def icon(self):
        return self._icon

    @icon.setter
    def icon(self, icon):
        try:
            self._icon = pygame.image.load(icon)
        except FileNotFoundError:
            self._icon = False
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        self._size = size
