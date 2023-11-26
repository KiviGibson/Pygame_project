import Game.game as game
import definition as df


def start_game() -> None:
    game.Game(df.ROOT_PATH)


if __name__ == "__main__":
    start_game()
