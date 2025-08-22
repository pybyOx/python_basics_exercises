
def create_list(my_list):
    quantity_exp = int(input('\nВведите кол-во экспериментов: '))
    for num in range(quantity_exp):
        print('Введите результат', num + 1, 'эксперимента:', end=' ')
        result_exp = int(input())
        my_list.append(result_exp)


exp_list = []

create_list(exp_list)
print('Список результатов всех экспериментов:', exp_list)

print('Четные числа в обратном порядке: ', end='')
for i in range(len(exp_list) - 1, -1, -1):
    if exp_list[i] % 2 == 0:
        print(exp_list[i], end=' ')
