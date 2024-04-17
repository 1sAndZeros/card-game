from lib.Game import Game
from lib.Player import Player
from lib.utils import clear

clear()

names = ["Rikie", "Alina", "Roberto", "Oli"]
players = [Player(i + 1, name) for i, name in enumerate(names)]

game = Game(players)
game.start_game()
