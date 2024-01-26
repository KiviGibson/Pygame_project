import Game.Objects.gameobject as gameobject
import Game.loader as loader
import Game.Objects.Components.Colliders.squere_collider as collider

class Coin(gameobject.GameObject):

    def __init__(self,pos):
        super().__init__((18, 18), pos)
        self.images = {
            "rotation": loader.Loader().load_image_array("/Images/Animations/coin", "png")
        }
        self.sounds = {
            "pick_up": loader.Loader().load_sound("/Sounds/pickup.wav")
        }
        self.collider = collider.SquereCollider((18,18),pos,self,True)
        self.diff = 4
        self.dir = 1
        self.frame = 0
        self.image = self.images["rotation"][self.frame]
        self.game = None

    def update(self, g):
        if self.game == None:
            self.game = g
        self.levitate()
        self.animte()

    def animte(self):
        self.frame += 0.1
        self.frame %= len(self.images["rotation"])
        self.image = self.images["rotation"][int(self.frame)]

    def levitate(self):
        if self.diff < 0:
            self.diff = 4
            self.dir = -self.dir
        self.mov_y = 0.2 * self.dir
        self.move(0, self.mov_y)
        self.diff -= 0.1

    def on_trigger(self, other):
        self.game.remove_game_object(self)
        self.sounds["pick_up"].play()
