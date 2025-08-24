
# def is_symmetry(my_list):      если нужно найти палиндром циклом
#     n = len(my_list)
#     for i in range(n // 2):
#         if my_list[i] != my_list[n - i - 1]:
#             return False
#     return True

def is_symmetry(my_list):
    return my_list == my_list[::-1]


numbers_list = [int(input(f'Число № {i + 1}: '))
                for i in range(int(input('Кол-во чисел: ')))]

print('\nПоследовательность:', numbers_list)

for i in range(len(numbers_list)):
    part = numbers_list[i:]
    if is_symmetry(part):
        to_add = numbers_list[:i][::-1]
        print('Нужно приписать чисел:', len(to_add))
        print('Сами числа:', to_add)
        break
