import Systems.game as game
import Pygame_project.definition as df


def start_game():
    obj = game.Game(df.ROOT_PATH)
    obj.start_game()


if __name__ == "__main__":
    start_game()
