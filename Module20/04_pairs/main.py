import random


def create_list():
    return [random.randint(0, 100) for _ in range(10)]

# альтернативное решение
# def change_list(my_list):
#     return [(my_list[index], my_list[index + 1]) for index in range(0, 10, 2)]


def change_list(my_list):
    return list(zip([value for index, value in enumerate(my_list) if index % 2 == 0],
                    [value for index, value in enumerate(my_list) if index % 2 != 0]))


original_list = create_list()
print('Оригинальный список:', original_list)
print('Новый список:', change_list(original_list))
