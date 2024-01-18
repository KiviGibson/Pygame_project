import Game.Objects.gameobject as gm
import Game.loader as loader
import Game.Objects.Player.squere_collider as sqere_collider
import Game.Objects.Player.player as player


class Projectile(gm.GameObject):
    def __init__(self, pos=(0, 0), direction=(0, 0), game=object(),dont=object()):
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
        self.game = game
        self.dont = dont

    def update(self, g):
        self.move()
        self.animate()

    def move(self):
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
            other.damage(self.game)
        del self

    def animate(self):
        self.frame += 0.2
        self.frame %= 2
        self.image = self.images["fireball"][int(self.frame)]
