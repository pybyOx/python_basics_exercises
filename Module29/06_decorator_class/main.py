import functools
import time
from typing import Callable, Any


class LoggerDecorator:
    """
    Декоратор класса для логирования вызовов функций и времени их выполнения.

    Этот декоратор оборачивает функцию и логирует информацию о ее вызове,
    аргументах, времени выполнения и результате.
    """
    def __init__(self, func: Callable[..., Any]) -> None:
        """Инициализирует декоратор.
        Args:
            func: Функция, которую нужно декорировать.
        """
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs) -> Any:
        """
        Вызывается при каждом вызове декорированной функции.
        Args:
            *args: Позиционные аргументы, переданные в функцию.
            **kwargs: Именованные аргументы, переданные в функцию.
        Returns:
            Результат вызова декорированной функции.
        """
        print('\n\tВызов функции {}\n{}\nАргументы: {},{}'.format(self.func.__name__, '_' * 40, args, kwargs))
        start_time = time.time()
        value = self.func(*args, **kwargs)
        end_time = time.time()
        print('Результат: {}\nВремя выполнения функции {} сек'.format(
            value, round(end_time - start_time, 3)))
        return value


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется сложный алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)
