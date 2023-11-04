from Game.Game import Game
from Objects.Player import Player


def start():
    game = Game(tickrate=60, name="Tiny Dino", size=(500, 600))
    player = Player((180, 260), game)
    game.addobject(player)
    game.start()


if __name__ == "__main__":
    start()
