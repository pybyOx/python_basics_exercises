from datetime import datetime as dt
from time import time
from functools import wraps
from typing import Callable


def timer(cls, func: Callable, date_format: str) -> Callable:
    """Декоратор метода класса, логирующий его работу и рассчитывающий время его работы"""
    @wraps(func)
    def wrapped_func(*args, **kwargs):
        new_format = ''.join('%{}'.format(sym) if sym.isalpha() else sym for sym in date_format)
        print('Запускается {}.{}. Дата и время запуска: {}.'.format(
            cls.__name__, func.__name__, dt.now().strftime(new_format)))
        start = time()
        result = func(*args, **kwargs)
        finish = time()
        print('Завершение {}.{}, время работы = {} s.'.format(
            cls.__name__, func.__name__, round(finish - start, 3)))
        return result

    return wrapped_func


def log_methods(date: str) -> Callable:
    """Декоратор, логирующий немагические методы класса."""
    def logger(cls):

        for method_name in dir(cls):
            if method_name.startswith("__") is False:
                method = getattr(cls, method_name)
                decorated_method = timer(cls, method, date)
                setattr(cls, method_name, decorated_method)

        return cls

    return logger


@log_methods('b d Y — H:M:S')
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods('b d Y - H:M:S')
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
