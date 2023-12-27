import gameobject
import game
import squere_collider
import loader
import pygame
import definition as df


class Gate(gameobject.GameObject):
    def __init__(self, size: tuple[float, float], position: tuple[float, float], game: game.Game, map: str, spawn: int):
        super().__init__(position=position, size=size, render=False)
        self.game = game
        self.map = map
        self.spawn = spawn
        self.collider = squere_collider.SquereCollider(size, position, self, trigger=True)
        img = loader.Loader(df.ROOT_PATH).load_image("/Images/arrow_right_curve", "png")
        ui = pygame.surface.Surface((32, 32), pygame.SRCALPHA)
        pygame.transform.scale(img, (32, 32), ui)
        self.ui_icon = gameobject.GameObject((32, 32), (position[0]-7, position[1]-32), img=ui)

    def on_collision(self, other) -> None:
        try:
            if other.parent.interact:
                self.game.change_map(self.map, self.spawn)
        except AttributeError:
            pass
