# TODO здесь писать код
def least_divisor(numeric):
    for divisor in range(2, numeric + 1):
        if numeric % divisor == 0:
            print('Наименьший делитель, отличный от единицы:', divisor)
            break


while True:
    number = int(input('Введите число больше 1: '))
    if number <= 1:
        print('Ошибка ввода. Попробуйте еще раз.')
        continue
    else:
        break
least_divisor(number)
