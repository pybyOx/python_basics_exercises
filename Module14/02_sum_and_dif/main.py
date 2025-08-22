# TODO здесь писать код
def sum_of_digits(numeric):
    sum_main = 0
    while numeric:
        last_digit = numeric % 10
        sum_main += last_digit
        numeric //= 10
    return sum_main


def quantity_of_digits(numeric):
    count = 0
    while numeric:
        count += 1
        numeric //= 10
    return count


while True:
    number = int(input('Введите целое положительное число: '))
    if number <= 0 or number % 1 != 0:
        print('Ошибка ввода. Попробуйте еще раз')
        continue
    else:
        break

sum_result = sum_of_digits(number)
quantity_result = quantity_of_digits(number)

print('Сумма чисел:', sum_result)
print('Количество цифр в числе:', quantity_result)
print('Разность суммы и количества цифр:', sum_result - quantity_result)
