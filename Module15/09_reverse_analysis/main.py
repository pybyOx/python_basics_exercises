# TODO здесь писать код

def create_list(my_list):
    quantity_exp = int(input('\nВведите кол-во экспериментов: '))
    for num in range(quantity_exp):
        print('Введите результат', num + 1, 'эксперимента:', end=' ')
        result_exp = int(input())
        my_list.append(result_exp)


def sort_list(my_list):
    for i_1 in range(len(my_list) - 1):
        maximum = i_1
        for i_2 in range(i_1, len(my_list)):
            if my_list[maximum] <= my_list[i_2]:
                maximum = i_2
        my_list[i_1], my_list[maximum] = my_list[maximum], my_list[i_1]


def remove_odd_numbers(my_list):
    for index in range(len(my_list)):
        if my_list[index] % 2 == 0:
            print(my_list[index], end=', ')


exp_list = []

create_list(exp_list)
# создали список результатов всех экспериментов
print('Список результатов всех экспериментов:', exp_list)

sort_list(exp_list)
# отсортировали результаты от большего к меньшему

print('Отсортированный список: ', end='')
remove_odd_numbers(exp_list)
# убрали нечетные числа
