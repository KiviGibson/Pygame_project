from Game import game
from Objects import player


def start():
    current_game = game.Game(tickrate=60, name="Tiny Dino", size=(500, 600))
    current_player = player.Player((180, 260), current_game, scale=3, skin="green")
    current_game.addobject(current_player)
    current_game.start()


if __name__ == "__main__":
    start()
