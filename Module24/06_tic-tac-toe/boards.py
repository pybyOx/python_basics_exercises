from cells import Cell


class Board:
    def __init__(self):
        self.info = [Cell(number) for number in range(1, 10)]

    def reset(self):
        for cell in self.info:
            cell.occupied = False
            cell.symbol = ''

    def change_cell(self, number, symbol):
        for cell in self.info:
            if cell.number == number and not cell.occupied:
                cell.occupied = True
                cell.symbol = symbol
                return True
        return False

    def check_game_over(self, moves_list):  # pycharm пишет 'may be 'static', что это значит и нужно ли исправлять?
        winner_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9],
                       [1, 4, 7], [2, 5, 8], [3, 6, 9],
                       [3, 5, 7], [1, 5, 9]]

        for numbers in winner_list:
            if len(moves_list) >= 3 and all(number in moves_list for number in numbers):
                return True
        return False
