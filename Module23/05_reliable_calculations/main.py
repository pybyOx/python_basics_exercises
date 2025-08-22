import math


def get_sage_sqrt(digit):
    try:
        result = math.sqrt(digit)
        return result
    except ValueError:
        print('Нельзя взять корень отрицательного значения.')
    except TypeError:
        print('Ошибка ввода: убедитесь, что переданное значение является числом.')
    except Exception:
        print('Неизвестная ошибка')


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}\n")
