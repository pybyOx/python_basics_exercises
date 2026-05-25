from boards import Board
from players import Player


class Game:
    """Класс, управляющий ходом игры.

    Attributes:
        gamers (list[Player]): Список игроков.
        board (Board): Игровое поле.
    """
    def __init__(self, player_1: Player, player_2: Player):
        """Создаёт игру.

        Args:
            player_1 (Player): Первый игрок.
            player_2 (Player): Второй игрок.
        """
        self.gamers = [player_1, player_2]
        self.board = Board()

    def main_menu(self):
        """Запускает основной цикл игры.

        В цикле последовательно запускаются игры.
        После каждой выводится текущий счёт.
        Игрокам предлагается продолжить или завершить.
        """
        continue_game = 'да'

        while continue_game == 'да':
            self.one_game()

            print('\nТекущий счет:')
            for gamer in self.gamers:
                print(f'{gamer.name}: {gamer.wins}')

            while True:
                continue_game = input('\nХотите начать новую игру? (да/нет): ').lower()
                if continue_game in ['да', 'нет']:
                    break

                print('Ошибка ввода: нужно ответить "да" или "нет".')

    def one_game(self):
        """Запускает одну игру.

        Игроки поочерёдно делают ходы.
        После каждого хода поле отображается в консоли.
        Победитель определяется при достижении выигрышной комбинации.

        """
        self.board.reset()
        players = self.gamers

        for turn in range(9):
            current_player = players[turn % 2]
            print(f"\nХодит {current_player.name}...")
            while True:
                number = current_player.move()
                if self.board.change_cell(number, current_player.symbol):
                    break
                print("Клетка занята, попробуйте снова.")

            self.board.display()

            if self.board.check_game_over(current_player.symbol):
                print(f"Победил {current_player.name}!")
                current_player.wins += 1
                return

        print('Ничья!')
