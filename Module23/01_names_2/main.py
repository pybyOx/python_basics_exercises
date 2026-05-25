sum_symbols = 0

with open('people.txt', 'r', encoding='utf-8') as people_file:

    for number, line in enumerate(people_file, start=1):

        name = line.strip()

        if len(name) < 3:
            msg = f'Ошибка: менее трёх символов в строке {number}.'
            print(msg)

            with open('errors.log', 'a', encoding='utf-8') as errors_file:
                errors_file.write(msg + '\n')

        sum_symbols += len(name)

print('Общее количество символов: {}.'.format(sum_symbols))
