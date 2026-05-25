amt_man = int(input('Кол-во человек: '))
periodicity = int(input('Какое число в считалке? '))
print(f'Значит, выбывает каждый {periodicity}-й человек')

man_list = list(range(1, amt_man + 1))

shift = periodicity - 1
index = 0
while len(man_list) > 1:

    print('\nТекущий круг людей:', man_list)
    print('Начало счёта с номера', man_list[index])

    index = (index + shift) % len(man_list)
    print('Выбывает человек под номером', man_list[index])

    man_list.remove(man_list[index])

    if index == len(man_list):
        index = 0

print('\nОстался человек под номером', man_list[index])
