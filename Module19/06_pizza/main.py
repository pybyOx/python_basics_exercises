def create_dictionary():
    order_count = int(input('Введите количество заказов: '))
    buyers_dictionary = dict()

    for digit in range(order_count):
        print('\n{}-й заказ: '.format(digit + 1), end='')
        customer_name, pizza_name, pizza_quantity = input('(Покупатель Название_пиццы Количество_заказанных_пицц)\n').title().split()
        pizza_quantity = int(pizza_quantity)
        if customer_name not in buyers_dictionary.keys():
            buyers_dictionary[customer_name] = {pizza_name: pizza_quantity}
        else:
            if pizza_name in buyers_dictionary[customer_name].keys():
                buyers_dictionary[customer_name][pizza_name] += pizza_quantity
            else:
                buyers_dictionary[customer_name][pizza_name] = pizza_quantity

    return buyers_dictionary


def output(my_dictionary):
    for name in my_dictionary.keys():
        print('\n{}:'.format(name))
        for pizza in my_dictionary[name].keys():
            print('{} - {} шт.'.format(pizza, my_dictionary[name][pizza]))


buyers = create_dictionary()

output(buyers)
