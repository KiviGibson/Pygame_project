from pygame import image, surface, mixer
import definition


class Loader:
    def __init__(self):
        self.ROOT_FOLDER = definition.ROOT_PATH

    def load_image(self, name: str, format: str) -> surface.Surface:
        img = image.load(self.ROOT_FOLDER+name+"."+format)
        return img

    def load_image_array(self, path_to_animation_folder: str, format: str) -> list:
        images = []
        counter = 0
        while True:
            try:
                images.append(image.load(f"{self.ROOT_FOLDER}{path_to_animation_folder}/{counter}.{format}"))
                counter += 1
            except FileNotFoundError:
                break
        return images

    def load_sound(self, path: str) -> mixer.Sound:
        try:
            return mixer.Sound(file=self.ROOT_FOLDER + path)
        except:
            return mixer.Sound(None)
