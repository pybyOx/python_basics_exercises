from functools import wraps
from _collections_abc import Callable


def counter(func: Callable) -> Callable:
    """Декоратор, считающий и выводящий количество вызовов декорируемой функции."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        print('Функция {} вызывалась {} раз.'.format(func.__name__, wrapper.count))
        return result

    wrapper.count = 0
    return wrapper
