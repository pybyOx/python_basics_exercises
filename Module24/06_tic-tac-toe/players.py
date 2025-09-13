class Player:
    """Класс, описывающий игрока.

    Attributes:
        name (str): Имя игрока.
        wins (int): Количество побед игрока.
        symbol (str): Символ, которым играет игрок ('X' или 'O').
    """
    def __init__(self, symbol: str):
        """Создаёт игрока.

        При создании запрашивает имя у пользователя.

       Args:
           symbol (str): Символ игрока ('X' или 'O').
       """
        self.name = input(f'Введите имя игрока ({symbol}): ')
        self.wins = 0
        self.symbol = symbol

    def move(self) -> int:
        """Запрашивает у игрока номер клетки.

        Returns:
            int: Номер клетки, выбранной игроком (от 1 до 9).
        """
        while True:
            try:
                number = int(input(f'{self.name}, введите номер клетки (1-9): '))
                if 1 <= number <= 9:
                    return number
                print('Ошибка ввода: введите число от 1 до 9.')
            except ValueError:
                print('Ошибка ввода: нужно ввести число.')
