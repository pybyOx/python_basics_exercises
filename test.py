try:
    ages_file = open('ages', 'r')
except IsADirectoryError:
    print('Указанный путь ведет к папке, а не файлу')

try:
    result_file = open('result.txt', 'x')
except FileExistsError:
    print('Такой файл уже существует')
