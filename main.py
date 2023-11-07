from Game import game
from Objects import player


def start():
    current_game = game.Game(tickrate=60, name="Tiny Dino", size=(500, 600))
    current_game.start()


if __name__ == "__main__":
    start()
