from pygame import image
import os

class Loader:
    ROOT_FOLDER = os.path.dirname(os.path.abspath(__file__))
    @classmethod
    def load_image(cls, name, type):
        print(cls.ROOT_FOLDER)
        img = image.load(cls.path_to_folder+name+type)
        return img

    @classmethod
    def load_image_array(cls, path_to_animation, type):
        images = []
        counter = 0
        while True:
            try:
                images.append(image.load(f"{cls.path_to_folder}{path_to_animation}/{counter}.{type}"))
                counter += 1
            except FileNotFoundError:
                break
        return images
