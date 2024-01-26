import Game.Objects.collisionobject as gameobject
import loader
import Game.Objects.Player.player as player
import pygame


class Jumper(gameobject.CollisionObject):
    def __init__(self, size=(30, 36), position=(0, 0), direction=False):
        self.images = {
            "idle": loader.Loader().load_image_array("/Images/Animations/yellow/idle", "png"),
            "jump": loader.Loader().load_image_array("/Images/Animations/yellow/jump", "png"),
            "death": loader.Loader().load_image_array("/Images/Animations/yellow/death", "png")
        }
        self.sounds = {
            "jump": loader.Loader().load_sound("/Sounds/jump.wav"),
            "hurt": loader.Loader().load_sound("/Sounds/damege.wav")
        }
        super().__init__(size, position, img=self.images["idle"][0], simulate=True)
        self.sounds["jump"].set_volume(0.3)
        self.frame = 0
        self.timer = 20
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
        self.move(self.mov_x, self.mov_y)
        self.collider.update(self.x, self.y)
        if self.windup():
            self.jump()
        self.animate()

    def animate(self):
        max_img = len(self.images[self.state])
        if self.state == "jump":
            self.frame += 0.2
            self.frame = min(self.frame, max_img-1)
        else:
            self.frame += 0.2
            self.frame %= max_img
        self.image = self.images[self.state][int(self.frame) % max_img]
        self.image = pygame.transform.flip(self.image, self.side, False)

    def windup(self) -> bool:
        if self.on_ground:
            if self.state == "jump" and self.current > 0:
                self.mov_x = 0
                self.side = not self.side
                self.state = "idle"
            else:
                self.current += 1
                if self.current >= self.timer:
                    return True
        return False

    def jump(self):
        self.state = "jump"
        self.frame = 0
        self.sounds["jump"].play()
        self.mov_y = -12.8
        self.current = 0
        self.mov_x = int(-(self.side-0.5)*2) * 2

    def on_collision(self, other):
        super().on_collision(other)
        if side := self.collider.check_side(other.collider) == self.collider.SIDES["down"]:
            if isinstance(other, player.Player):
                other.jump(force=True)
            self.sounds["hurt"].play()
            self.game.remove_game_object(self)
            del self
        elif side == self.collider.SIDES["top"]:
            if isinstance(other, player.Player):
                other.damage()
