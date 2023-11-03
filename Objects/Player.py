from Objects.GameObject import GameObject
from Game.Renderer import Renderer
from Game.Input import Input

class Player(GameObject):
    def __init__(self, position, sprite):
        super().__init__(position, "Player")
        self.renderer = Renderer((self.transform.scale, self.transform.scale), imagePath=sprite)
        self.input = Input()

    def draw(self):
        self.renderer.draw(self.transform.position[0], self.transform.position[1])

    def walk(self,mult=1,speed=5):
        move = ((self.input.x_axis * speed, self.input.y_axis * speed))
        self.transform.move(move)