from pygame import image, surface


class Loader:
    def __init__(self, root: str):
        self.ROOT_FOLDER = root

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
