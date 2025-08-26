import os


with open('numbers.txt', 'r', encoding='utf-8') as file:
    total = sum(int(x) for x in file.read().split())


with open('answer.txt', 'w', encoding='utf-8') as summ_file:
    summ_file.write(str(total))


def read_file(file_name):
    print(f'Содержимое файла {file_name}')
    with open(os.path.abspath(file_name), 'r', encoding='utf-8') as f:
        print('\n', f.read())


read_file('numbers.txt')
read_file('answer.txt')
