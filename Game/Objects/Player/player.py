import pygame

import Game.game as game
import definition as df
import loader
from Game.Objects import gameobject
from squere_collider import SquereCollider


class Player(gameobject.GameObject): 
    SPEED = 4

    def __init__(self, size=(30, 36), position=(0, 0)) -> None:
        self.images = {
            "idle": loader.Loader(df.ROOT_PATH).load_image_array("/Images/Animations/green/idle", "png"),
            "walk": loader.Loader(df.ROOT_PATH).load_image_array("/Images/Animations/green/walk", "png")
        }
        self.sounds = {
            "jump": loader.Loader(df.ROOT_PATH).load_sound("/Sounds/jump.wav"),
            "walk": loader.Loader(df.ROOT_PATH).load_sound("/Sounds/walk.wav"),
            "hit_ground": loader.Loader(df.ROOT_PATH).load_sound("/Sounds/hit_ground.wav")
        }
        self.sounds["walk"].set_volume(0.05)
        self.sounds["hit_ground"].set_volume(0.3)
        self.sounds["jump"].set_volume(0.3)
        super().__init__(size, position, img=self.images["idle"][0])
        self.mov_x: float = 0
        self.mov_y: float = 0
        self.collider: SquereCollider = SquereCollider(size, (self.x, self.y), self)
        self.can_jump: int = 0
        self.state = "idle"
        self.side: bool = False
        self.image_index: float = 0
        self.coyote_time_duration: int = 5
        self.on_ground: bool = True
        self.interact: bool = False

    def update(self, g) -> None:
        for event in g.events:
            if event.type == pygame.KEYDOWN:
                self.press_button(event.key)
            elif event.type == pygame.KEYUP:
                self.release_button(event.key)
        x, y = self.calculate_movement()
        x, y = self.collide(g, x, y)
        self.move(x, y)
        if self.on_ground:
            self.can_jump = self.coyote_time_duration
        else:
            self.can_jump -= 1
        self.collider.update(self.x, self.y)
        self.stomp()
        self.animate(x)

    def press_button(self, button: int) -> None:
        match button:
            case pygame.K_d:
                self.mov_x += 1
            case pygame.K_a:
                self.mov_x -= 1
            case pygame.K_SPACE:
                self.jump()
            case pygame.K_e:
                self.interact = True

    def release_button(self, button: int) -> None:
        match button:
            case pygame.K_d:
                self.mov_x -= 1
            case pygame.K_a:
                self.mov_x += 1
            case pygame.K_e:
                self.interact = False

    def collide(self, g, x_dir, y_dir) -> tuple[float, float]:
        on_g = False
        for obj in self.collider.collide_with(g):
            x, y, first_side, second_side = self.collider.check_direction(obj.collider)
            try:
                self.x = float(x)
                if first_side:
                    x_dir = min(x_dir, 0)
                if second_side:
                    x_dir = max(x_dir, 0)
            except TypeError:
                self.y = float(y)
                if first_side:
                    y_dir = min(y_dir, 0)
                    on_g = True
                if second_side:
                    y_dir = max(y_dir, 0)
        if self.on_ground != on_g and on_g is True:
            self.play("hit_ground")
        self.on_ground = on_g
        self.mov_y = y_dir
        return x_dir, y_dir

    def calculate_movement(self) -> tuple[float, float]:
        y = self.mov_y + game.Game.GRAVITY
        x = self.mov_x * Player.SPEED
        return x, y

    def move(self, x, y) -> None:
        self.x += x
        self.y += y
        self.change_sprite_pos()

    def jump(self) -> None:
        if self.can_jump > 0:
            self.play("jump")
            self.can_jump = 0
            self.mov_y = -12.8

    def change_sprite_pos(self) -> None:
        self.rect.x = self.x
        self.rect.y = self.y

    def change_animations(self,x):
        if x != 0:
            self.state = "walk"
            if x < 0:
                self.side = True
            else:
                self.side = False
        else:
            self.state = "idle"
            
    def animate(self, x):
        self.change_animations(x)
        max_img = len(self.images[self.state])
        self.image = self.images[self.state][int(self.image_index) % max_img]
        self.image = pygame.transform.flip(self.image, self.side, False)
        self.image_index += 0.2
        self.image_index %= max_img
    def stomp(self):
        if self.state == "walk" and round(self.image_index, 2) % 3.0 == 0 and self.on_ground is True:
            self.play("walk")

    def play(self, name: str) -> None:
        self.sounds[name].play()
