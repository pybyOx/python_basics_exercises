import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
print('Первая команда:', first_team)

second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
print('\nВторая команда:', second_team)

winners = [max(first_team[index], second_team[index]) for index in range(20)]
print('\nПобедители тура:', winners)
