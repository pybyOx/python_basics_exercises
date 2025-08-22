import os


def open_file(file_name):
    print('Содержимое файла {}'.format(file_name))
    my_file = open(os.path.abspath(file_name), 'r', encoding='utf-8')
    print('\n', my_file.read())
    my_file.close()


def count_summ(file_name):
    my_file = open(os.path.abspath(file_name), 'r', encoding='utf-8')
    numbers_list = [int(digit) for line in my_file for digit in line.split()]
    my_file.close()
    return sum(numbers_list)


summ_file = open('answer.txt', 'w')
summ_file.write(str(count_summ('numbers.txt')))
summ_file.close()

open_file('numbers.txt')
open_file('answer.txt')
