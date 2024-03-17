import pygame

import Game.loader as loader
import Game.Objects.collisionobject as collisionobject


class Player(collisionobject.CollisionObject):
    def __init__(self, size=(30, 36), position=(0, 0)) -> None:
        self.images = {
            "idle": loader.Loader().load_image_array("/Images/Animations/green/idle", "png"),
            "walk": loader.Loader().load_image_array("/Images/Animations/green/walk", "png"),
            "damage": loader.Loader().load_image_array("/Images/Animations/green/damage", "png")
        }
        self.sounds = {
            "jump": loader.Loader().load_sound("/Sounds/jump.wav"),
            "walk": loader.Loader().load_sound("/Sounds/walk.wav"),
            "hit_ground": loader.Loader().load_sound("/Sounds/hit_ground.wav"),
            "hurt": loader.Loader().load_sound("/Sounds/damege.wav")
        }
        super().__init__(size, position, img=self.images["idle"][0], simulate=True)
        self.can_jump: int = 0
        self.state = "idle"
        self.side: bool = False
        self.image_index: float = 0
        self.coyote_time_duration: int = 7
        self.jump_buffer: int = 7
        self.on_ground: bool = False
        self.interact: bool = False
        self.pressed_a = False
        self.pressed_d = False
        self.game = None

    def update(self, g) -> None:
        if self.game is None:
            self.game = g
            for key in self.sounds:
                self.sounds[key].set_volume(g.volume)
        for event in g.events:
            if event.type == pygame.KEYDOWN:
                self.press_button(event.key)
            elif event.type == pygame.KEYUP:
                self.release_button(event.key)
        self.set_movement()
        x = self.calculate_movement()
        self.mov_y = self.gravity(self.mov_y, self.on_ground)
        self.move(x, self.mov_y)
        if self.on_ground:
            self.can_jump = self.coyote_time_duration
            if self.jump_buffer > 0:
                self.jump()
                self.jump_buffer = 0
        else:
            self.jump_buffer -= 1
            self.can_jump -= 1
        self.collider.update(self.x, self.y)
        self.stomp()
        self.animate(x)

    def press_button(self, button: int) -> None:
        match button:
            case pygame.K_d:
                self.pressed_d = True
            case pygame.K_a:
                self.pressed_a = True
            case pygame.K_SPACE:
                self.jump_buffer = 7
            case pygame.K_e:
                self.interact = True

    def release_button(self, button: int) -> None:
        match button:
            case pygame.K_d:
                self.pressed_d = False
            case pygame.K_a:
                self.pressed_a = False
            case pygame.K_e:
                self.interact = False

    def set_movement(self):
        x = 0
        if self.pressed_a:
            x -= 1
        if self.pressed_d:
            x += 1
        self.mov_x = x

    def jump(self, force=False) -> None:
        if self.can_jump > 0 or force:
            self.play("jump")
            self.can_jump = 0
            self.mov_y = -12.8

    def change_animations(self, x):
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
        self.sounds[name].set_volume(self.game.volume)
        self.sounds[name].play()

    def damage(self):
        self.sounds["hurt"].play()
        self.image = self.images["damage"][1]
        self.game.swap_time = True
