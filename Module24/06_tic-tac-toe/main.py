from players import Player
from games import Game


def main():
    """Создаёт двух игроков, запускает игру и отображает меню."""
    gamer_1 = Player('X')
    gamer_2 = Player('O')
    game = Game(gamer_1, gamer_2)
    game.main_menu()


if __name__ == '__main__':
    main()
