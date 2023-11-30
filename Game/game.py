import pygame

import definition
from Game.Objects.Player.player import Player


class Game:

    # Global values
    GRAVITY = 0.3

    def __init__(self, definition):
        pygame.init()
        player = Player()   # create player
        self.root_dir = definition.ROOT_PATH
        self.running = False
        self.game_objects = pygame.sprite.Group()
        self.game_objects.add(player)
        self.objects = [player]
        self.events = []
        self.clock = pygame.time.Clock()
        self.start_game()

    def start_game(self) -> None:
        """
        startup function before game loop starts
        """
        self.running = True
        pygame.display.set_mode((500, 500))
        while self.running:
            self.update()
        pygame.quit()

    def update(self) -> None:
        """
        update state of the game, gameobjects
        """
        self.events = [e for e in pygame.event.get()]

        for go in self.objects:
            go.update(self.events)

        self.check_quit()
        self.render()
        self.clock.tick(120)
        print(self.clock.get_fps())

    def check_quit(self) -> None:
        """
        check if player want to exit, then close the game
        """
        if pygame.QUIT in [e.type for e in self.events]:
            self.running = False


    def render(self) -> None:
        """
        draw a new frame
        """
        pygame.display.get_surface().fill((0, 0, 0))
        self.game_objects.draw(pygame.display.get_surface())
        pygame.display.flip()
