shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

name_detail = input('Название детали: ')

count = 0
total_price = 0

for index_1 in range(len(shop)):
    if shop[index_1][0] == name_detail:
        count += 1
        total_price += shop[index_1][1]

print('Кол-во деталей:', count)

print('Общая стоимость:', total_price)
