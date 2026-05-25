def add_shift(old_list: list) -> list:
    return [numbers[i - shift] for i in range(len(old_list))]


numbers = [1, 4, -3, 0, 10]

shift = int(input('Сдвиг: '))

print('Изначальный список:', numbers)

numbers = add_shift(numbers)

print('Сдвинутый список:', numbers)
