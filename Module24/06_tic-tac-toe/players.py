class Player:
    def __init__(self, symbol):
        self.name = input('Введите имя игрока: ')
        self.wins = 0
        self.symbol = symbol
        self.moves = []

    def move(self):
        while True:
            try:
                number = int(input(f'{self.name}, введите номер клетки: '))
                if number in range(1, 10):
                    return number
                else:
                    print('Ошибка ввода: номер клетки должен находиться в диапазоне от 1 до 9.')
            except ValueError:
                print('Ошибка ввода: необходимо ввести число.')
