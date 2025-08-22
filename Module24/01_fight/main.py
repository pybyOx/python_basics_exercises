import random


class Unit:

    def __init__(self, name):
        self.name = name
        self.health = 100

    def is_alive(self):
        return self.health > 0

    def hit(self, other_unit):
        other_unit.health -= 20
        print('\n{} атакует! У {} осталось здоровья: {}'.format(
            self.name, other_unit.name, other_unit.health))

    def fight(self, other_unit):

        while self.is_alive() and other_unit.is_alive():
            attacker = random.choice([self, other_unit])
            defender = self if attacker == other_unit else other_unit
            attacker.hit(defender)

        if self.health == 0:
            print('Игрок {} одержал победу!'.format(other_unit.name))
        else:
            print('Игрок {} одержал победу!'.format(self.name))


unit_1 = Unit('Воин 1')
unit_2 = Unit('Воин 2')
print('Начинаем бой!')
unit_1.fight(unit_2)
