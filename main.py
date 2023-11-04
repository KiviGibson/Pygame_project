from Game.Game import Game
from Objects.Player import Player


def start():
    game = Game(tickrate=60, name="Tiny Dungeon", size=(500, 600))
    player = Player((180, 260), "./Animations/Player/idle/0.png", game)

    game.addobject(player)

    game.start()


if __name__ == "__main__":
    start()
