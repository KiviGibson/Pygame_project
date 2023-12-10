import pygame
import map


class Game:
    # Global values
    GRAVITY = 1
    SCALE = 1

    def __init__(self, definition: any) -> None:
        pygame.init()
        self.root_dir = definition.ROOT_PATH
        self.running = False
        self.game_objects = pygame.sprite.Group()
        self.objects = []
        self.events = []
        self.clock = pygame.time.Clock()
        self.map_manager = map.Map()
        self.frame = pygame.surface.Surface((1000, 1000))
        self.scaled = pygame.surface.Surface((self.frame.get_width() * Game.SCALE, self.frame.get_height() * Game.SCALE))
        self.start_game()

    def start_game(self) -> None:
        """
        startup function before game loop starts
        """
        self.running = True
        pygame.display.set_mode(self.frame.get_size())
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
        self.clock.tick(60)

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
                if event.key == pygame.K_0:
                    print(self.clock.get_fps())

    def render(self) -> None:
        """
        create a new frame, then scale it and draw it on screen
        """
        self.frame.fill((0, 0, 0))
        [self.frame.blit(layer, (0, 0)) for layer in self.map_manager.backLayer]
        self.game_objects.draw(self.frame)
        [self.frame.blit(layer, (0, 0)) for layer in self.map_manager.frontLayer]
        pygame.display.get_surface().fill((0, 0, 0))
        pygame.transform.scale(self.frame, self.scaled.get_size(), self.scaled)
        pygame.display.get_surface().blit(self.scaled, (0, 0))
        pygame.display.flip()
