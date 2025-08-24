
def create_dictionary():
    buyers_dictionary = dict()

    for i in range(int(input('Введите количество заказов: '))):
        while True:
            order = input(f'{i + 1}-й заказ: ').title().split()
            if len(order) == 3:
                customer_name, pizza_name, pizza_quantity = order
                if pizza_quantity.isdigit():
                    cust_dict = buyers_dictionary.setdefault(customer_name, {})
                    cust_dict[pizza_name] = cust_dict.get(pizza_name, 0) + int(pizza_quantity)
                    break
            print('Некорректный ввод. '
                  '\nНеобходимо ввести заказ в виде:'
                  '\n<Покупатель> <Название пиццы> <Количество заказанных пицц>')

    return buyers_dictionary


def output(my_dictionary):
    for name in sorted(my_dictionary):  
        print(f'{name}:')
        for pizza in sorted(my_dictionary[name]):  # сортировка пицц
            print(f'\t{pizza}: {my_dictionary[name][pizza]}')


buyers = create_dictionary()

output(buyers)
