n = int(input('Введите число: '))
odd_numbers = [num for num in range(1, n + 1) if num % 2 != 0]
print('Список из нечётных чисел от одного до N:', odd_numbers)
