def read_info(file_name):
    with open(file_name, 'r', encoding='utf-8') as my_file:
        for line in my_file:
            line = line.replace('\n', '')
            try:
                error = check_info(line)
                if error is None:
                    with open('registrations_good.log', 'a', encoding='utf-8') as good_info:
                        good_info.write(line + '\n')
                else:
                    with open('registrations_bad.log', 'a', encoding='utf-8') as bad_info:
                        bad_info.write(line + '  -  ' + error + '\n')
            except Exception as unknown_error:
                print('Неизвестная ошибка:', unknown_error)


def check_info(string):
    try:
        if len(string.split()) != 3:
            raise IndexError('НЕ присутствуют все три поля')

        name, mail, age = string.split()

        if not name.isalpha():
            raise NameError('Поле «Имя» содержит НЕ только буквы')
        if '@' not in mail or '.' not in mail:
            raise SyntaxError('Поле «Имейл» НЕ содержит @ и/или точку')
        age = int(age)
        if not 10 <= age <= 99:
            raise ValueError('Поле «Возраст» НЕ представляет число от 10 до 99')

    except (IndexError, NameError, SyntaxError, ValueError) as error:
        return str(error)
        # print('{}:{}.'.format(error, exp))

    return None


def print_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as my_file:
            print('\nСодержимое файла {}:\n{}\n{}'.format(file_name, '_' * 40, my_file.read()))
    except FileNotFoundError:
        print('Файл {} не найден'.format(file_name))


read_info('registrations.txt')
print_file('registrations_good.log')
print_file('registrations_bad.log')
