class Cell:
    """Класс, описывающий одну клетку игрового поля.

    Attributes:
        number (int): Номер клетки (от 1 до 9).
        occupied (bool): Флаг, показывающий, занята ли клетка.
        symbol (str): Символ игрока, занявшего клетку ('X' или 'O').
    """
    def __init__(self, number: int):
        """Создаёт клетку.

        Args:
            number (int): Номер клетки (от 1 до 9).
        """
        self.number = number
        self.occupied = False
        self.symbol = ''
