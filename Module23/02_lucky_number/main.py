import random


def create_errors_list():
    with open('errors.txt', 'r', encoding='utf-8') as errors_file:
        return errors_file.read().split('\n')


def write_numbers(errors, sum_numbers=0):
    try:
        with open('out_file.txt', 'a') as numbers_file:

            while sum_numbers < 777:

                number = int(input('Введите число: '))
                sum_numbers += number

                if 13 == random.randint(1, 13):
                    raise Exception

                numbers_file.write(str(number) + '\n')

            print('Вы успешно выполнили условие для выхода из порочного цикла!')

    except Exception:
        print('\n{}: Вас постигла неудача!'.format(random.choice(errors)))


def read_file(file_name):
    print('\nСодержимое файла {}:'.format(file_name))
    with open(file_name) as my_file:
        print(my_file.read())


errors_list = create_errors_list()
write_numbers(errors_list)
read_file('out_file.txt')
