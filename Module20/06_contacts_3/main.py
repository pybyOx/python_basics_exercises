def add_contact(contacts):
    name, surname = input('Введите имя и фамилию нового контакта (через пробел): ').title().split()
    number = input('Введите номер телефона: ')
    if (name, surname) in contacts:
        print('Такой контакт существует.')
    else:
        contacts[(name, surname)] = number
    print(f'Текущий словарь контактов: {contacts}')
    return contacts


def find_contact():
    user_surname = input('Введите фамилию для поиска: ').title()
    count = 0
    for contact, user_number in contact_dictionary.items():
        if contact[1] == user_surname:
            print(f'{contact[0]} {contact[1]} - {user_number}')
            count += 1
    if count == 0:
        print('Контакта с такой фамилией нет в словаре.')


contact_dictionary = dict()
while True:
    choice = int(input('\nВведите номер действия:\n    1.Добавить контакт\n    2.Найти человека\n'))
    if choice == 1:
        add_contact(contact_dictionary)
    elif choice == 2:
        find_contact()
    else:
        print('Ошибка ввода')
