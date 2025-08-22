def create_dictionary():
    order_count = int(input('Введите количество заказов: '))
    buyers_dictionary = dict()

    for digit in range(order_count):
        print('{}-й заказ: '.format(digit + 1), end='')
        order_list = input('(Покупатель Название_пиццы Количество_заказанных_пицц)\n').title().split()
        if order_list[0] not in buyers_dictionary.keys():
            buyers_dictionary[order_list[0]] = {order_list[1]: int(order_list[2])}
        else:
            if order_list[1] in buyers_dictionary[order_list[0]].keys():
                buyers_dictionary[order_list[0]][order_list[1]] += int(order_list[2])
            else:
                buyers_dictionary[order_list[0]][order_list[1]] = int(order_list[2])

    return buyers_dictionary


def output(my_dictionary):
    for name in my_dictionary.keys():
        print('\n{}:'.format(name))
        for pizza in my_dictionary[name].keys():
            print('{} - {} шт.'.format(pizza, my_dictionary[name][pizza]))


buyers = create_dictionary()

output(buyers)
