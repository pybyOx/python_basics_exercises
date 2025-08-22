numbers = [1, 4, -3, 0, 10]

shift = int(input('Сдвиг: '))

numbers_shift = [numbers[i - shift] for i in range(len(numbers))]

print('Изначальный список:', numbers)
print('Сдвинутый список:', numbers_shift)
