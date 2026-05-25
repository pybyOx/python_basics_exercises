guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while len(guests) > 0:

    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)

    print('Гость пришёл или ушёл?', end=' ')
    came_or_went = input().lower()

    if came_or_went == 'пришёл' or came_or_went == 'пришел':
        print('Имя гостя:', end=' ')
        name_guest = input().title()

        if len(guests) < 6:
            print('Привет,', name_guest)
            guests.append(name_guest)
        else:
            print('Прости,', name_guest, 'но мест нет')

    elif came_or_went == 'ушёл' or came_or_went == 'ушел':

        print('Имя гостя:', end=' ')
        name_guest = input()

        print('Пока,', name_guest, '!')
        guests.remove(name_guest)

    elif came_or_went == 'пора спать':
        print('Вечеринка закончилась, все легли спать.')
        break

    else:
        print('Ошибка ввода')
else:
    print('\nВсе гости разошлись!')
