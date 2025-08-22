amt_man = int(input('Кол-во человек: '))
periodicity = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый', periodicity, '-й человек')

man_list = list(range(1, amt_man + 1))

i = 0
while len(man_list) > 1:

    print('\nТекущий круг людей:', man_list)
    print('Начало счёта с номера', man_list[i])

    for _ in range(periodicity - 1):
        if i == len(man_list) - 1:
            i = 0
        else:
            i += 1

    print('Выбывает человек под номером', man_list[i])

    man_list.remove(man_list[i])

    if i == len(man_list):
        i = 0

print('\nОстался человек под номером', man_list[i])
