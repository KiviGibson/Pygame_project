import Game.Objects.collisionobject as gm
import Game.loader as loader
import pygame
import Game.Objects.Player.player as player
import Game.Objects.Box.box as box


class Walkie(gm.CollisionObject):
    def __init__(self, size=(36, 36), position=(0, 0), direction=False):
        self.images = {
            "idle": loader.Loader().load_image_array("/Images/Animations/blue/idle", "png"),
            "walk": loader.Loader().load_image_array("/Images/Animations/blue/walk", "png"),
            "death": loader.Loader().load_image_array("/Images/Animations/blue/death","png")
        }
        self.sounds = {
            "walk": loader.Loader().load_sound("/Sounds/walk.wav"),
            "hurt": loader.Loader().load_sound("/Sounds/damege.wav")
        }
        super().__init__(size, position, img=self.images["idle"][0], simulate=True)
        self.game: object = None
        self.frame = 0
        self.timer = 120
        self.current = 0
        self.delay = 30
        self.side = direction
        self.on_ground = True
        self.state = "idle"
        self.max_left = 0
        self.max_right = 0

    def update(self, g):
        if self.game is None:
            self.game = g
        self.mov_y = self.gravity(self.mov_y, self.on_ground)
        self.walk()
        self.move(self.mov_x, self.mov_y)
        self.animate()
        self.collider.update(self.x, self.y)

    def walk(self):
        if self.on_ground:
            self.mov_x = int(-(self.side-0.5)*2) * 2
            self.state = "walk"
            if self.x > self.max_right - 32:
                self.side = True
            elif self.x < self.max_left:
                self.side = False
        else:
            self.state = "idle"
            self.mov_x = 0

    def animate(self):
        self.frame += 0.2
        self.frame %= len(self.images[self.state])
        self.image = self.images[self.state][int(self.frame)]
        self.image = pygame.transform.flip(self.image, self.side, False)

    def on_collision(self, other):
        super().on_collision(other)
        if side := self.collider.check_side(other.collider) == self.collider.SIDES["down"]:
            if isinstance(other, player.Player):
                other.jump(force=True)
            self.sounds["hurt"].play()
            self.game.remove_game_object(self)
            del self
        elif side == self.collider.SIDES["top"] and isinstance(other, box.Box):
            self.max_left = other.collider.left
            self.max_right = other.collider.right
        else:
            if isinstance(other, player.Player):
                other.damage()
