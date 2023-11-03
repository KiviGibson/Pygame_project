from Game.Game import Game
from Objects.Player import Player
game = Game()
player = Player((20, 20), "")
game.startup()
game.addobject(player)
game.adduserobject(player)
game.start()
