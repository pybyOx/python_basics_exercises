import random


def fight(unit, other_unit):
    while unit.is_alive() and other_unit.is_alive():
        attacker = random.choice([unit, other_unit])
        defender = unit if attacker == other_unit else other_unit
        attacker.hit(defender)

    if unit.health == 0:
        print('Игрок {} одержал победу!'.format(other_unit.name))
    else:
        print('Игрок {} одержал победу!'.format(unit.name))


class Unit:

    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def defense(self):
        self.health -= 20

    def hit(self, other_unit):
        other_unit.defense()
        print('\n{} атакует! У {} осталось здоровья: {}'.format(
            self.name, other_unit.name, other_unit.health))


unit_1 = Unit('Воин 1')
unit_2 = Unit('Воин 2')
print('Начинаем бой!')
fight(unit_1, unit_2)
