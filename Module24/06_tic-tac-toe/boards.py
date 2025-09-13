from cells import Cell


class Board:
    """Класс, описывающий поле игры.

    Attributes:
        info (list[Cell]): Поле игры в виде списка объектов Cell.
    """
    def __init__(self):
        """Создаёт поле из 9 клеток."""
        self.info: list[Cell] = []
        self.reset()

    def reset(self):
        """Сбрасывает поле в начальное состояние.

        Все клетки становятся свободными, их символ очищается.
        """
        self.info = [Cell(number) for number in range(1, 10)]

    def display(self):
        """Выводит поле в консоль.

        Каждая свободная клетка отображается своим номером,
        а занятая — символом игрока.
        """
        print()
        for i in range(0, 9, 3):
            row = [cell.symbol if cell.occupied else str(cell.number)
                   for cell in self.info[i:i + 3]]
            print(" | ".join(row))
        print()

    def change_cell(self, number: int, symbol: str) -> bool:
        """Пытается изменить клетку.

        Args:
            number (int): Номер клетки от 1 до 9.
            symbol (str): Символ игрока ('X' или 'O').

        Returns:
            bool: True, если клетка успешно изменена,
            иначе False (если клетка уже занята).
        """
        cell = self.info[number - 1]
        if not cell.occupied:
            cell.occupied = True
            cell.symbol = symbol
            return True
        return False

    def check_game_over(self, symbol: str) -> bool:
        """Проверяет, завершена ли игра для указанного символа.

        Метод перебирает все возможные выигрышные комбинации
        (строки, столбцы и диагонали) и проверяет, заняты ли все
        позиции в комбинации данным символом.

        Args:
            symbol (str): Символ игрока, для которого проверяется победа ("X" или "O").

        Returns:
            bool: True, если игрок с данным символом победил, иначе False.
        """
        winner_list = [
            [1, 2, 3], [4, 5, 6], [7, 8, 9],  # строки
            [1, 4, 7], [2, 5, 8], [3, 6, 9],  # столбцы
            [1, 5, 9], [3, 5, 7]  # диагонали
        ]

        for numbers in winner_list:
            if all(self.info[n - 1].symbol == symbol for n in numbers):
                return True
        return False
