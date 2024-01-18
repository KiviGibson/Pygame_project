import Game.Objects.collisionobject as gm
import Game.loader as loader
import Game.Objects.Projectile.projectile as projectile
import Game.Objects.Player.player as player
import pygame


class Dragon(gm.CollisionObject):
    def __init__(self, size=(36, 36), position=(0, 0), direction=False):
        self.images = {
            "idle": loader.Loader().load_image_array("/Images/Animations/red/idle", "png"),
            "atack": loader.Loader().load_image_array("/Images/Animations/red/idle_run", "png"),
            "death": loader.Loader().load_image_array(".Image/Animations/red/","png")
        }
        self.sounds = {
            "achoo": loader.Loader().load_sound("/Sounds/fire.wav"),
            "hurt": loader.Loader().load_sound("/Sounds/damege.wav")
        }
        self.sounds["achoo"].set_volume(0.3)
        super().__init__(size, position, img=self.images["idle"][0], simulate=True)
        self.game: object = None
        self.frame = 0
        self.timer = 120
        self.current = 0
        self.delay = 30
        self.side = direction
        self.on_ground = True
        self.state = "idle"

    def update(self, g):
        if self.game is None:
            self.game = g
        self.collider.update(self.x, self.y)
        self.mov_y = self.gravity(self.mov_y, self.on_ground)
        self.move(0, self.mov_y)
        self.animate()
        if self.windup():
            self.atack(g)

    def animate(self):
        if self.state == "atack":
            self.delay -= 1
            if self.delay == 0:
                self.delay = 30
                self.state = "idle"
        self.frame += 0.2
        self.frame %= len(self.images[self.state])
        self.image = self.images[self.state][int(self.frame)]
        self.image = pygame.transform.flip(self.image, self.side, False)

    def windup(self) -> bool:
        self.current += 1
        if self.current > self.timer:
            return True
        return False

    def atack(self, game):
        self.sounds["achoo"].play()
        self.current = -30
        self.state = "atack"
        game.add_game_object(projectile.Projectile((self.x, self.y+15), ((0.5-self.side) * 2, 0), game=game,dont=self))
        print("Achooo!")

    def on_collision(self, other):
        super().on_collision(other)
        if self.collider.check_side(other.collider) == self.collider.SIDES["down"]:
            if isinstance(other, player.Player):
                other.jump(force=True)
            self.sounds["hurt"].play()
            self.game.remove_game_object(self)
            del self
