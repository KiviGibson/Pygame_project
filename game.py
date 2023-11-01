from pygame import *
import options
class Game:
    def __init__(self):
        self.running = True
        self.option = options.Option("Game Title", "", (400, 500))

    def start(self):
        self.startup()
        while self.running:
            for e in event.get():
                draw.rect(display.get_surface(), (255, 0, 0), Rect(30, 30, 60, 60))
                if e.type == QUIT:
                    self.running = False
            display.flip()
    def startup(self):
        option = self.option

        display.set_mode(option.size)

        surface = display.get_surface()
        color = (20, 20, 20)
        surface.fill(color)

        display.set_caption(option.title)

        if option.icon:
            icon = image.load(option.icon)
            display.set_icon(icon)