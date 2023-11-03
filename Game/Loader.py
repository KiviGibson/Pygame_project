from pygame import *


class Loader:
    def __init__(self, path_to_folder="./"):
        self.path = path_to_folder
        self._image = set()

    def loadimage(self, name, type):
        if img := self.searchimage(name) is not None:
            img = image.load(self.path+name+type)
            self._images.add({name: name, sprite: img})
            return img
        else:
            return img

    def searchimage(self, name):
        for img in self._image:
            if img.name == name:
                return img.sprite
        return None
