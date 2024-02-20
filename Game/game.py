import pygame
import Game.map as map
import Game.Objects.gameobject as gameobject
import Game.Objects.Player.player as player
import definition as df
import loader
import Game.save_system as save_system


class Game:
    # Global values
    GRAVITY = 0.8
    SCALE = 1.5

    def __init__(self, definition: any) -> None:
        pygame.init()
        self.save_system = save_system.SaveSystem()
        self.font = pygame.font.Font(df.ROOT_PATH + "/Images/AtariClassic-gry3.ttf", 48)
        self.root_dir = definition.ROOT_PATH
        self.running = False
        self.game_objects = pygame.sprite.Group()
        self.objects: list[gameobject.GameObject] = []
        self.events = []
        self.clock = pygame.time.Clock()
        self.map_manager = map.Map(self)
        self.frame = pygame.surface.Surface((1260, 1260), pygame.SRCALPHA)
        self.camera_pos = [0, 0]
        self.scaled = pygame.surface.Surface(
            (self.frame.get_width() * Game.SCALE,
             self.frame.get_height() * Game.SCALE))
        self.target: gameobject.GameObject | None = None
        self.screen_cover = self.create_cover()
        self.cover_pos = 0
        self.swap_time = False
        self.hide = True
        self.current_map = ()
        self.next_map = ()
        self.coins = 0
        self.start_game()

    @staticmethod
    def create_cover() -> pygame.surface.Surface:        
        return loader.Loader().load_image("/Images/cover", "png")

    def start_game(self) -> None:
        """
        startup function before game loop starts
        """
        self.running = True
        pygame.display.set_mode((1000, 1000))
        self.change_map("test", 0)
        self.load_data()
        while self.running:
            self.update()
        pygame.quit()

    def test(self) -> None:
        self.swap_time = True

    def change_map(self, m: str, s: int):
        self.next_map = self.root_dir + self.map_manager.maps[m], s
        self.swap_time = True

    def swap_map(self) -> None:
        """
        changes maps
        """
        data_to_save = {
            "stats": {
                "coins": str(self.coins)
            }
        }
        self.save_system.save_data(data_to_save)
        self.map_manager.load_map(*self.next_map)

    def load_data(self):
        try:
            saved_data = self.save_system.load_save_data()
            self.coins = int(saved_data["stats"]["coins"])
        except TypeError:
            pass

    def reload_map(self):
        if self.hide and self.transition_hide():
            if not (self.next_map == self.current_map):
                self.current_map = self.next_map
                self.swap_map()
            self.hide = False
            self.dump_objects()
            self.load_data()
            for obj in self.map_manager.get_objects():
                self.add_game_object(obj)
                try:
                    if isinstance(obj, player.Player):
                        self.change_camera_target(obj)
                        self.change_camera_position(self.target, snap=False)
                except ValueError:
                    pass
        if not self.hide and self.transition_show():
            self.swap_time = False
            self.hide = True

    def transition_hide(self) -> bool:
        if self.cover_pos <= -50:
            return True
        self.cover_pos -= 5
        self.cover_pos = max(-50, self.cover_pos)
        return False

    def transition_show(self) -> bool:
        if self.cover_pos <= -100:
            self.cover_pos = 100
            return True
        self.cover_pos -= 5
        self.cover_pos = max(-100, self.cover_pos)
        return False

    def update(self) -> None:
        """
        update state of the game, gameobjects
        """
        self.events = [e for e in pygame.event.get()]
        if self.swap_time:
            self.reload_map()
        else:
            for go in self.objects:
                go.update(self)
                if go.simulate:
                    go.sim(self)
        self.change_camera_position(self.target)
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
        text = self.font.render(f"{self.coins}", True, (255, 255, 255))
        pygame.display.get_surface().fill(self.map_manager.color)
        self.frame.fill(self.map_manager.color)
        [self.frame.blit(layer, (0, 0)) for layer in self.map_manager.backLayer]
        self.game_objects.draw(self.frame)
        [self.frame.blit(layer, (0, 0)) for layer in self.map_manager.frontLayer]
        pygame.transform.scale(self.frame, self.scaled.get_size(), self.scaled)
        pygame.display.get_surface().fill((0, 0, 0))
        pygame.display.get_surface().blit(self.scaled, self.camera_pos)
        pygame.display.get_surface().blit(text, (10, 10))
        pygame.display.get_surface().blit(self.screen_cover, (self.screen_cover.get_width() * (self.cover_pos/100), -200))
        pygame.display.flip()

    def change_camera_target(self, obj: gameobject.GameObject):
        self.target = obj

    def change_camera_position(self, target: gameobject.GameObject, snap=False):
        try:
            width, height = pygame.display.get_window_size()
            max_x = -self.frame.get_width() + width / (self.SCALE * 1.8)
            max_y = -self.frame.get_height() + height / (self.SCALE * 1.8)
            pos_x = min(max(-target.x * Game.SCALE + target.rect.width / 2 + width / 2, max_x), 0)
            pos_y = min(max(-target.y * Game.SCALE + target.rect.height / 2 + height / 2, max_y), 0)
            if not snap:
                pos_x = df.lerp(self.camera_pos[0], pos_x, 0.125)
                pos_y = df.lerp(self.camera_pos[1], pos_y, 0.125)
            self.camera_pos = [pos_x, pos_y]
        except AttributeError:
            print("Cant find object!")

    def add_game_object(self, o: gameobject.GameObject):
        if o.render:
            self.game_objects.add(o)
        self.objects.append(o)

    def remove_game_object(self, target: gameobject.GameObject):
        self.objects.pop(self.objects.index(target))
        self.game_objects.remove(target)

    def dump_objects(self):
        self.objects = []
        self.game_objects = pygame.sprite.Group()

    def find_object_by_id(self, index=-1) -> gameobject.GameObject:
        for ob in self.objects:
            try:
                if int(ob.index) == index:
                    return ob
            except AttributeError:
                pass
        raise ValueError(f"Can't find object with id {index}")

    def collect_coin(self):
        self.coins += 1
