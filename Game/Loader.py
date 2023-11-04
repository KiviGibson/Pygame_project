from pygame import *


class Loader:
    def __init__(self, path_to_folder="C:/Users/popla/PycharmProjects/pygame/Pygame_project/Animations"):
        self.path_to_folder = path_to_folder
        self._image = set()

    def loadimage(self, name, type):
        if img := self.searchimage(name) is not None:
            img = image.load(self.path+name+type)
            self._images.add({name: name, sprite: img})
            return img
        else:
            return img

    def loadimageArray(self, path_to_animation, type):
        images = []
        counter = 0
        while True:
            try:
                images.append(image.load(f"{self.path_to_folder}{path_to_animation}/{counter}.{type}"))
                counter += 1
            except FileNotFoundError:
                break
        return images

    def searchimage(self, name):
        for img in self._image:
            if img.name == name:
                return img.sprite
        return None
