from random import randint


class House:
    def __init__(self, food, money):
        self.fridge = food
        self.money = money


class Human:
    def __init__(self, name, home: House):
        self.name = name
        self.full = 50
        self.house = home

    def eat(self):
        self.full += 10
        self.house.fridge -= 10
        print(f'{self.name} ест.')

    def work(self):
        self.full -= 10
        self.house.money += 10
        print(f'{self.name} работает.')

    def play(self):
        self.full -= 10
        print(f'{self.name} играет.')

    def store(self):
        self.house.fridge += 10
        self.house.money -= 10
        print(f'{self.name} идет в магазин.')

    def day(self):
        number = randint(1, 6)

        if self.house.fridge >= 10 and self.full < 20:
            self.eat()
        elif self.house.money >= 10 and self.house.fridge < 10:
            self.store()
        elif self.full >= 10 and self.house.money < 50:
            self.work()
        elif number == 1 and self.full >= 10:
            self.work()
        elif number == 2 and self.house.fridge >= 10:
            self.eat()
        else:
            self.play()

        if self.full > 0:
            return True

        print(f'{self.name} мертв/а')
        return False


def main():
    house = House(50, 0)

    human_1 = Human('Маша', house)
    human_2 = Human('Толя', house)

    for day in range(1, 366):
        print(f'\n{day} день:')

        if human_1.day() and human_2.day():
            print(
                f'Итог:\n'
                f'{human_1.name} (сытость: {human_1.full})\n'
                f'{human_2.name} (сытость: {human_2.full})\n'
                f'Еда: {house.fridge}\n'
                f'Деньги: {house.money}'
            )
        else:
            print('Game over')
            break


if __name__ == '__main__':
    main()
