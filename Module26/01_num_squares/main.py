def get_number() -> int:
    while True:
        try:
            max_number = int(input('Введите число: '))
        except ValueError:
            print('Необходимо ввести число!')
        else:
            break
    return max_number
