import Game.Objects.collisionobject as gm
import Game.loader as loader
import Game.Objects.Components.Colliders.squere_collider as sqere_collider
import Game.Objects.Player.player as player


class Projectile(gm.CollisionObject):
    def __init__(self, pos=(0, 0), direction=(0, 0), game=object(), dont=object()):
        self.images = {
            "fireball": loader.Loader().load_image_array("/Images/Animations/fireball", "png"),
            "explosion": loader.Loader().load_image_array("/Images/Animations/explosion", "png")
        }
        self.sounds = {
            "explode": loader.Loader().load_sound("/Sounds/explosion.wav")
        }
        super().__init__((18, 18), pos, img=self.images["fireball"][0])
        self.collider: sqere_collider.SquereCollider = sqere_collider.SquereCollider((18, 18), (self.x, self.y), self, trigger=True)
        self.frame: float = 0
        self.dir = direction
        self.side = False
        self.speed = 3.0
        self.lifetime = 300
        self.game = game
        for key in self.sounds:
            self.sounds[key].set_volume(game.volume)
        self.dont = dont

    def update(self, g):
        self.move(0, 0)
        self.animate()
        self.lifetime -= 1
        if self.lifetime < 0:
            self.end_of_lifecycle()

    def move(self, x, y):
        x, y = self.dir
        self.x += x * self.speed
        self.y += y * self.speed
        self.rect.x = self.x
        self.rect.y = self.y

    def on_trigger(self, other):
        if self.dont is other:
            return
        self.sounds["explode"].play()
        self.game.remove_game_object(self)
        if isinstance(other, player.Player):
            other.damage()
        del self

    def end_of_lifecycle(self):
        self.game.remove_game_object(self)
        del self

    def animate(self):
        self.frame += 0.2
        self.frame %= 4
        self.image = self.images["fireball"][int(self.frame)]
