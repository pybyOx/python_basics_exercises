from random import choice
from boards import Board


class Game:
    def __init__(self, player_1, player_2):
        self.gamers = [player_1, player_2]
        self.board = Board()

    def main_menu(self, continue_game=''):

        while continue_game != 'нет':

            first_mover = choice(self.gamers)
            other = self.gamers[1 - self.gamers.index(first_mover)]
            print('\nПервый ход делает {}.'.format(first_mover.name))

            if self.one_game(first_mover, other):

                print('\nТекущий счет:\n{}: {}\n{}: {}'.format(
                    self.gamers[0].name, self.gamers[0].wins,
                    self.gamers[1].name, self.gamers[1].wins))

            while True:
                continue_game = input('\nХотите начать новую игру? ').lower()
                if continue_game in ['да', 'нет']:
                    break
                else:
                    print('Ошибка ввода: нужно ответить "да" или "нет"')

    def one_game(self, player_1, player_2):

        self.board.reset()
        player_1.moves.clear()
        player_2.moves.clear()

        for player in [player_1, player_2] * 4 + [player_1]:
            if self.make_move(player):
                print('Победил/а {}!'.format(player.name))
                player.wins += 1
                return True

        print('\nНичья!')
        return False

    def make_move(self, player):
        while True:
            print('\nХодит {}...'.format(player.name))
            number = player.move()

            if self.board.change_cell(number, player.symbol):
                print('{} походил/а  на клетку {}'.format(player.name, number))
                player.moves.append(number)
                if self.board.check_game_over(player.moves):
                    return True
                else:
                    return False

            else:
                print('Не получилось сделать ход. Клетка уже занята')
