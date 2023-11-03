from Game.Game import Game
from Objects.Player import Player

game = Game(tickrate=120, name="Tiny Dungeon", size=(500, 600))
player = Player((20, 20), "")

game.addobject(player)
game.adduserobject(player)
game.start()
