import pygame
import map
import gameobject
import player


class Game:
    # Global values
    GRAVITY = 0.8
    SCALE = 1.5

    def __init__(self, definition: any) -> None:
        pygame.init()
        self.root_dir = definition.ROOT_PATH
        self.running = False
        self.game_objects = pygame.sprite.Group()
        self.objects = []
        self.events = []
        self.clock = pygame.time.Clock()
        self.map_manager = map.Map(self)
        self.frame = pygame.surface.Surface((1260, 1260), pygame.SRCALPHA)
        self.camera_pos = [0, 0]
        self.scaled = pygame.surface.Surface((self.frame.get_width() * Game.SCALE, self.frame.get_height() * Game.SCALE))
        self.target: gameobject.GameObject | None = None
        self.start_game()

    def start_game(self) -> None:
        """
        startup function before game loop starts
        """
        self.running = True
        pygame.display.set_mode((1000, 1000))
        self.change_map(map.Map.TEST_MAP, 0)
        while self.running:
            self.update()
        pygame.quit()

    def test(self) -> None:
        self.change_map(map.Map.TEST2_MAP, 1)

    def change_map(self, m: str, s: int) -> None:
        """
        changes maps
        """
        self.objects = []
        del self.game_objects
        self.game_objects = pygame.sprite.Group()
        self.map_manager.load_map(self.root_dir + m, s)
        for obj in self.map_manager.objects:
            self.objects.append(obj)
            try:
                if isinstance(obj, player.Player):
                    self.change_camera_target(obj)
                    self.change_camera_position(self.target, snap=False)
                if obj.render:
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
        self.change_camera_position(self.target)
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
        pygame.display.get_surface().fill(self.map_manager.color)
        self.frame.fill(self.map_manager.color)
        [self.frame.blit(layer, (0, 0)) for layer in self.map_manager.backLayer]
        self.game_objects.draw(self.frame)
        [self.frame.blit(layer, (0, 0)) for layer in self.map_manager.frontLayer]
        pygame.display.get_surface().fill((0, 0, 0))
        pygame.transform.scale(self.frame, self.scaled.get_size(), self.scaled)
        pygame.display.get_surface().blit(self.scaled, self.camera_pos)
        pygame.display.flip()

    def change_camera_target(self, obj: gameobject.GameObject):
        self.target = obj

    def change_camera_position(self, target: gameobject.GameObject, snap=False):
        try:
            width, height = pygame.display.get_window_size()
            max_x = -self.frame.get_width() + width / 2
            max_y = -self.frame.get_height() + height / 2
            pos_x = min(max(-target.x * Game.SCALE + target.rect.width / 2 + width / 2, max_x), 0)
            pos_y = min(max(-target.y * Game.SCALE + target.rect.height / 2 + height / 2, max_y), 0)
            if not snap:
                pos_x = self.lerp(self.camera_pos[0], pos_x, 0.125)
                pos_y = self.lerp(self.camera_pos[1], pos_y, 0.125)
            self.camera_pos = [pos_x, pos_y]
        except ValueError:
            print("Cant find object!")

    @staticmethod
    def lerp(a: float, b: float, t: float):
        return (1 - t) * a + b * t
