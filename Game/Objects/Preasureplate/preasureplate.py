import Game.Objects.gameobject as gm
import Components.Colliders.squere_collider as collider
import Game.Objects.Listener.observer as observer
import loader


class PreasurePlate(gm.GameObject):

    def __init__(self, size, position, index=-1):
        super().__init__(size, position)
        self.images = {
            "pressed": loader.Loader().load_image("/Images/preassure_pad/pressed", "png"),
            "not_pressed": loader.Loader().load_image("/Images/preassure_pad/not_pressed", "png")
        }
        self.sounds = {
            "click": loader.Loader().load_sound("/Sounds/click.wav")
        }
        self.collider = collider.SquereCollider(size, position, self, True)
        self.observer = observer.Observer("step_on", "continuous")
        self.image = self.images["not_pressed"]
        self.triggered = False
        self.cooldown = 0
        self.index = index

    def update(self, g):
        if self.triggered:
            self.cooldown -= 1
            if self.cooldown < 0:
                self.image = self.images["not_pressed"]
                self.triggered = False

    def animate(self):
        ...

    def on_trigger(self, other):
        if not self.triggered:
            self.observer.activate_event("step_on")
            self.triggered = True
            self.sounds["click"].play()
        else:
            self.observer.activate_event("continuous")
        self.image = self.images["pressed"]
        self.cooldown = 5