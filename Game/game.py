import pygame
import map


class Game:
    # Global values
    GRAVITY = 0.01

    def __init__(self, definition: any):
        pygame.init()
        self.root_dir = definition.ROOT_PATH
        self.running = False
        self.game_objects = pygame.sprite.Group()
        self.objects = []
        self.events = []
        self.clock = pygame.time.Clock()
        self.map_manager = map.Map()
        self.start_game()

    def start_game(self) -> None:
        """
        startup function before game loop starts
        """
        self.running = True
        pygame.display.set_mode((1000, 1000))
        self.change_map(map.Map.TEST_MAP)
        while self.running:
            self.update()
        pygame.quit()

    def test(self) -> None:
        self.change_map(map.Map.TEST2_MAP)

    def change_map(self, m: str) -> None:
        """
        changes maps
        """
        self.objects = []
        del self.game_objects
        self.game_objects = pygame.sprite.Group()
        self.map_manager.load_map(self.root_dir + m)
        for obj in self.map_manager.objects:
            self.objects.append(obj)
            try:
                self.game_objects.add(obj)
            except ValueError:
                pass

    def update(self) -> None:
        """
        update state of the game, gameobjects
        """
        self.events = [e for e in pygame.event.get()]

        for go in self.objects:
            go.update(self)
        self.check_quit()
        self.render()
        self.clock.tick(120)
        #  print(self.clock.get_fps())

    def check_quit(self) -> None:
        """
        check if player want to exit, then close the game
        """
        if pygame.QUIT in [e.type for e in self.events]:
            self.running = False
        for event in self.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.test()

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
