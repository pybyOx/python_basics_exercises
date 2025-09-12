def read_info(file_name):
    with (open(file_name, 'r', encoding='utf-8') as my_file,
          open('registrations_good.log', 'w', encoding='utf-8') as good_file,
          open('registrations_bad.log', 'w', encoding='utf-8') as bad_file):

        for line in my_file:
            line = line.strip()
            try:
                check_info(line)
                good_file.write(line + '\n')
            except Exception as error:
                bad_file.write(line + '\t' + str(error) + '\n')


def check_info(string):
    if len(string.split()) != 3:
        raise IndexError('НЕ присутствуют все три поля')

    name, mail, age = string.split()

    if not name.isalpha():
        raise NameError('Поле «Имя» содержит НЕ только буквы')
    if '@' not in mail or '.' not in mail:
        raise SyntaxError('Поле «Имейл» НЕ содержит @ и/или точку')
    if not age.isdigit() or not 10 <= int(age) <= 99:
        raise ValueError('Поле «Возраст» НЕ представляет число от 10 до 99')


def print_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as my_file:
            print(f'\nСодержимое файла {file_name}:\n{'_' * 40}\n{my_file.read()}')
    except FileNotFoundError:
        print(f'Файл {file_name} не найден')


read_info('registrations.txt')
print_file('registrations_good.log')
print_file('registrations_bad.log')
