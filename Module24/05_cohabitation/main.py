from random import randint


class House:
    def __init__(self, food, money):
        self.fridge = food
        self.money = money


class Human:
    def __init__(self, name, home):
        self.name = name
        self.full = 50
        self.house = home

    def eat(self):
        self.full += 10
        self.house.fridge -= 10
        print('{} ест.'.format(self.name))

    def work(self):
        self.full -= 10
        self.house.money += 10
        print('{} работает.'.format(self.name))

    def play(self):
        self.full -= 10
        print('{} играет.'.format(self.name))

    def store(self):
        self.house.fridge += 10
        self.house.money -= 10
        print('{} идет в магазин.'.format(self.name))

    def day(self, number=randint(1, 6)):

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

        if self.full >= 0:
            return True
        else:
            print('{} мертв/а'.format(self.name))
            return False


house = House(50, 0)

human_1 = Human('Маша', house)
human_2 = Human('Толя', house)

for day in range(1, 366):

    print('\n{} день:'.format(day))
    if human_1.day() and human_2.day():
        print('Итог:\n{}(сытость: {})\n{}(сытость: {})\nEда: {}\nДеньги: {}'.format(
            human_1.name, human_1.full, human_2.name, human_2.full, house.fridge, house.money))
    else:
        print('Game over')
        break
