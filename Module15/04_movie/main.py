films = ['Крепкий орешек', 'Назад в будущее', 'Таксист',
         'Леон', 'Богемская рапсодия', 'Город грехов',
         'Мементо', 'Отступники', 'Деревня']
favorites = []

count = int(input('Сколько фильмов хотите добавить? '))

for _ in range(count):
    name = input('Введите название фильма: ')
    if name in films:
        favorites.append(name)
    else:
        print(f'Ошибка: фильма {name} у нас нет :(')

print('Ваш список любимых фильмов:', favorites)
