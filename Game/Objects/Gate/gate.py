import Game.Objects.gameobject as gameobject
import Game.Objects.Components.Colliders.squere_collider as squere_collider
import Game.loader as loader
import pygame


class Gate(gameobject.GameObject):
    def __init__(self, size: tuple[float, float], position: tuple[float, float], game: object, map: str, spawn: int):
        self.images = {
            "flag": loader.Loader().load_image_array("/Images/Animations/flag", "png")
        }
        super().__init__(position=position, size=size, img=self.images["flag"][0])
        self.game = game
        self.map = map
        self.spawn = spawn
        self.collider = squere_collider.SquereCollider(size, position, self, trigger=True)
        self.frame = 0

    def update(self, g):
        self.animate()

    def animate(self):
        self.frame += 0.1
        self.frame %= len(self.images["flag"])
        self.image = self.images["flag"][int(self.frame)]

    def on_trigger(self, other) -> None:
        print("trigger!")
        try:
            if other.interact:
                self.game.change_map(self.map, self.spawn)
        except AttributeError:
            pass
