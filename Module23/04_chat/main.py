def user_request():
    while True:
        user_name = input('\nВведите имя пользователя: ').title()
        while True:
            print(f'\n{user_name}, выберите действие:'
                  f'\n    1.Посмотреть текущий текст чата.'
                  f'\n    2.Отправить сообщение.'
                  f'\n    3.Сменить пользователя.'
                  f'\n  (Введите < 1 >, < 2 > или < 3 > )')
            try:
                user_selection = int(input())

                if user_selection == 1:
                    read_chat()
                elif user_selection == 2:
                    write_text(user_name)
                elif user_selection == 3:
                    break
                else:
                    raise ValueError

            except ValueError:
                print('Ошибка ввода: необходимо ввести < 1 >, < 2 > или < 3 > .')


def read_chat():
    try:
        with open('chat.txt', 'r', encoding='utf-8') as chat_file:
            print('Текущее содержание чата:\n{}'.format(chat_file.read()))
    except FileNotFoundError:
        print('Файл не найден')


def write_text(name):
    letter = input('Введите сообщение: ')
    try:
        with open('chat.txt', 'a', encoding='utf-8') as chat_file:
            chat_file.write('{}: {}\n'.format(name, letter))
    except FileNotFoundError:
        print('Файл не найден')


user_request()
