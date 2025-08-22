def add_contact(contacts):
    name, surname, number = input('Введите имя, фамилию и номер телефона (через пробел):').title().split()
    if (name, surname) in contacts:
        print('Такой контакт существует.')
    else:
        contacts[(name, surname)] = number
    print('Текущий список контактов:')
    for contact, user_number in contacts.items():
        print('   {} {} - {}'.format(contact[0], contact[1], user_number))
    return contacts


def find_contact(dictionary):
    user_surname = input('Введите фамилию: ').title()
    count = 0
    for contact, user_number in dictionary.items():
        if user_surname in contact and contact[1] == user_surname:
            print('{} {} - {}'.format(contact[0], contact[1], user_number))
            count += 1
    if count == 0:
        print('Контакта с такой фамилией нет в словаре.')


contact_dictionary = dict()
while True:
    choice = int(input('\nВведите номер действия:\n    1.Добавить контакт\n    2.Найти человека\n'))
    if choice == 1:
        add_contact(contact_dictionary)
    elif choice == 2:
        find_contact(contact_dictionary)
    else:
        print('Ошибка ввода')
