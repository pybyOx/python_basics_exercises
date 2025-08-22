from players import Player
from games import Game

gamer_1, gamer_2 = Player('X'), Player('O')
game = Game(gamer_1, gamer_2)
game.main_menu()
