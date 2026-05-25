
array_1 = [1, 5, 10, 20, 40, 80, 100]

array_2 = [6, 7, 20, 80, 100]

array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

set1, set2, set3 = set(array_1), set(array_2), set(array_3)

print(f'\nЗадача 1: элементы, которые есть в каждом списке'
      f'\nРешение без множеств: {[digit for digit in array_1 if digit in array_2 and digit in array_3]}'
      f'\nРешение с множествами: {sorted(set1 & (set2 & set3))}')

print(f'\nЗадача 2: элементы из первого списка, которых нет во втором и третьем списках'
      f'\nРешение без множеств: {[digit for digit in array_1 if digit not in array_2 and digit not in array_3]}'
      f'\nРешение с множествами: {sorted(set1 - (set2 | set3))}')
