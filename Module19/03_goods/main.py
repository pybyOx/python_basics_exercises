def counting_goods_and_prices(my_list):
    quantity = 0
    total_price = 0
    for slot in my_list:
        quantity += slot.get('quantity')
        total_price += slot.get('price') * slot.get('quantity')

    return quantity, total_price


def calculation(name, code, storage):
    quantity, total_price = counting_goods_and_prices(storage.get(code))
    print('{} - {} штук, стоимость {} руб.'.format(name, quantity, total_price))


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}

for product in goods.keys():
    calculation(product, goods.get(product), store)
