import gameobject
import game
import squere_collider


class Gate(gameobject.GameObject):
    def __init__(self,size: tuple[float, float], position: tuple[float, float], game: game.Game, map: str, spawn: int):
        super().__init__(position=position, size=size, render=False)
        self.game = game
        self.map = map
        self.spawn = spawn
        self.collider = squere_collider.SquereCollider(size, position, self, trigger=True)

    def on_collision(self, other) -> None:
        try:
            if other.parent.interact:
                self.game.change_map(self.map, self.spawn)
        except AttributeError:
            pass