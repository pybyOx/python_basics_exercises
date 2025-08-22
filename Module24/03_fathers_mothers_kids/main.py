from random import choice


class Parent:
    def __init__(self):
        self.name = input('Имя: ')
        self.age = int(input('Возраст: '))
        self.children = list()
        number_of_children = int(input('Количество детей: '))
        for number in range(number_of_children):
            print('\nИнформация о {} ребенке: '.format(number + 1))
            self.children.append(Child(self.age))

    def check_children(self):

        for child in self.children:

            print('\nКак там {}?'.format(child.name))

            if child.condition['Сытость'] is False:
                print('Ребенок голоден!')
                if input('Покормить? ').lower() == 'да':
                    child.feed_baby()
            if child.condition['Спокойствие'] is False:
                print('Ребенок плачет!')
                if input('Успокоить? ').lower() == 'да':
                    child.calm_child()
            if all(child.condition.values()):
                print('Ребенок сыт и спокоен.')


class Child:
    def __init__(self, parent_age):
        self.name = input('Имя ребенка: ')
        while True:
            self.age = int(input('Возраст ребенка: '))
            if (parent_age - self.age) >= 16:
                break
            else:
                print('Возраст ребенка должен быть меньше возраста родителя хотя бы на 16 лет')

        self.condition = {'Сытость': choice([True, False]), 'Спокойствие': choice([True, False])}

    def feed_baby(self):
        print('\nКормим ребенка ...')
        self.condition['Сытость'] = True

    def calm_child(self):
        print('\nУспокаиваем ребенка ...')
        self.condition['Спокойствие'] = True


print('Введите информацию о себе: ')
parent = Parent()
if input('\nХотите проверить детей? ').lower() == 'да':
    parent.check_children()
