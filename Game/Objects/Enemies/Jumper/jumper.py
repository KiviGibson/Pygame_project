import Game.Objects.collisionobject as gameobject
import loader
import Game.Objects.Player.player as player
import pygame


class Jumper(gameobject.CollisionObject):
    def __init__(self, size=(30, 36), position=(0, 0), direction=False):
        self.images = {
            "idle": loader.Loader().load_image_array("/Images/Animations/yellow/idle"),
            "jump": loader.Loader().load_image_array("/Images/Animations/yellow/jump"),
            "death": loader.Loader().load_image_array("/Images/Animations/yellow/death")
        }
        self.sounds = {
            "jump": loader.Loader().load_sound("Sounds/jump.wav")
        }
        super().__init__(size, position, img=self.images["idle"][0], simulate=True)
        self.sounds["jump"].set_volume(0.3)
        self.frame = 0
        self.timer = 80
        self.current = 0
        self.side = direction
        self.on_ground = True
        self.state = "idle"
        self.game: object = None
        self.player = None
    def update(self, g):
        if self.game is None:
            self.game = g
        self.mov_y = self.gravity(self.mov_y, self.on_ground)
        if self.windup():
            self.jump()

    def animate(self):
        max_img = len(self.images[self.state])
        self.image = self.images[self.state][int(self.frame) % max_img]
        self.image = pygame.transform.flip(self.image, self.side, False)
        self.frame += 0.2
        self.frame %= max_img

    def windup(self) -> bool:
        if self.on_ground:
            if self.state == "jump":
                self.state = "idle"
            self.current += 1
            return False
        return True

    def jump(self):
        self.state = "jump"
        self.sounds["jump"].play()
        self.mov_y = -12.8
        self.current = 0

    def on_collision(self, other):
        super().on_collision(other)
        if self.collider.check_side(other.collider) == self.collider.SIDES["down"]:
            if isinstance(other, player.Player):
                other.jump(force=True)
            self.sounds["hurt"].play()
            self.game.remove_game_object(self)
            del self
