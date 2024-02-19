import Game.Objects.gameobject as gameobject
import Game.Objects.Components.Colliders.squere_collider as squere_collider
import Game.loader as loader
import pygame


class Gate(gameobject.GameObject):
    def __init__(self, size: tuple[float, float], position: tuple[float, float], game: object, map: str, spawn: int):
        super().__init__(position=position, size=size, render=False)
        self.game = game
        self.map = map
        self.spawn = spawn
        self.collider = squere_collider.SquereCollider(size, position, self, trigger=True)
        img = loader.Loader().load_image("/Images/arrow_right_curve", "png")
        ui = pygame.surface.Surface((32, 32), pygame.SRCALPHA)
        pygame.transform.scale(img, (32, 32), ui)
        self.ui_icon = gameobject.GameObject((32, 32), (position[0]-7, position[1]-32), img=ui)

    def on_trigger(self, other) -> None:
        print("trigger!")
        try:
            if other.interact:
                self.game.change_map(self.map, self.spawn)
        except AttributeError:
            pass
