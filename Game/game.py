import pygame
from player import Player
from map import Map

class Game:

    # Global values
    GRAVITY = 0.3

    def __init__(self, definition: any):
        pygame.init()
        player: pygame.sprite.Sprite = Player()  # create player
        self.root_dir = definition.ROOT_PATH
        self.running = False
        self.game_objects = pygame.sprite.Group()
        self.game_objects.add(player)
        self.objects = [player]
        self.events = []
        self.clock = pygame.time.Clock()
        self.map_manager = Map()
        self.start_game()

    def start_game(self) -> None:
        """
        startup function before game loop starts
        """
        self.running = True
        pygame.display.set_mode((1000, 1000))
        self.map_manager.load_map(self.root_dir + Map.TEST_MAP)
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
        frame = pygame.surface.Surface((1000, 1000))
        [frame.blit(layer, (0, 0)) for layer in self.map_manager.backLayer]
        self.game_objects.draw(frame)
        [frame.blit(layer, (0, 0)) for layer in self.map_manager.frontLayer]
        pygame.display.get_surface().fill((0, 0, 0))
        pygame.display.get_surface().blit(frame, (0, 0))
        pygame.display.flip()
