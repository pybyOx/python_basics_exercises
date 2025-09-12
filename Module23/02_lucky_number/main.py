import random


def write_numbers():
    sum_numbers = 0
    try:
        with open('out_file.txt', 'w', encoding='utf-8') as numbers_file:
            while sum_numbers < 777:
                number = int(input('Введите число: '))
                sum_numbers += number

                numbers_file.write(f"{number}\n")

                if random.randint(1, 13) == 13:
                    raise Exception("Вас постигла неудача!")

            print("Вы успешно выполнили условие для выхода из порочного цикла!")
    except Exception as e:
        print(e)


def read_file(file_name):
    print(f"\nСодержимое файла {file_name}:")
    with open(file_name, 'r', encoding='utf-8') as f:
        print(f.read())


write_numbers()
read_file('out_file.txt')