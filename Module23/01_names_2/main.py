sum_symbols = 0

with open('people.txt', 'r', encoding='utf-8') as people_file:

    for number, string in enumerate(people_file, start=1):

        string = string.replace('\n', '')

        if len(string) < 3:
            print('Ошибка: менее трёх символов в строке {}.'.format(number))

            with open('errors.log', 'a', encoding='utf-8') as errors_file:
                errors_file.write(string + '\n')

        sum_symbols += len(string)

    print('Общее количество символов: {}.'.format(sum_symbols))
