import Game.Objects.gameobject as gm
import Game.Objects.Components.Colliders.squere_collider as collider
import Game.loader as loader


class PreasurePlate(gm.GameObject):

    def __init__(self, size, position, targets:str, methods:str, params:str):
        super().__init__(size, position)
        self.images = {
            "pressed": loader.Loader().load_image("/Images/preassure_pad/pressed", "png"),
            "not_pressed": loader.Loader().load_image("/Images/preassure_pad/not_pressed", "png")
        }
        self.sounds = {
            "click": loader.Loader().load_sound("/Sounds/click.wav")
        }
        self.collider = collider.SquereCollider(size, position, self, True)
        self.image = self.images["not_pressed"]
        self.triggered = False
        self.cooldown = 0
        self.targets = targets.strip().split(", ")
        self.methods = methods.strip().split(", ")
        self.params = params.strip().split(", ")
        self.listeners = []
        self.game = None

    def update(self, g):
        if self.game == None:
            self.game = g
            for key in self.sounds:
                self.sounds[key].set_volume(g.volume)
            self.find_targets()
        if self.triggered:
            self.cooldown -= 1
            if self.cooldown < 0:
                self.image = self.images["not_pressed"]
                self.triggered = False

    def animate(self):
        ...

    def on_trigger(self, other):
        if not self.triggered:
            for listener, params in self.listeners:
                listener(params)
            self.triggered = True
            self.sounds["click"].play()
        self.image = self.images["pressed"]
        self.cooldown = 5

    def find_targets(self):
        zipped = zip(self.targets, self.methods, self.params)
        for element in zipped:
            self.listeners.append((self.game.find_object_by_id(int(element[0])).funcs[element[1]], element[2].strip(" ")))
