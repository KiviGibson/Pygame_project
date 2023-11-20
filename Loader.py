from pygame import *


class Loader:
    def __init__(self, path_to_folder="C:/Users/popla/PycharmProjects/pygame/Pygame_project/Animations"):
        self.path_to_folder = path_to_folder
        self._image = set()

    def load_image(self, name, type):
        if img := self.search_image(name) is not None:
            img = image.load(self.path_to_folder+name+type)
            self._image.add({name: name, sprite: img})
            return img
        else:
            return img

    def load_image_array(self, path_to_animation, type):
        images = []
        counter = 0
        while True:
            try:
                images.append(image.load(f"{self.path_to_folder}{path_to_animation}/{counter}.{type}"))
                counter += 1
            except FileNotFoundError:
                break
        return images

    def search_image(self, name):
        for img in self._image:
            if img.name == name:
                return img.sprite
        return None
