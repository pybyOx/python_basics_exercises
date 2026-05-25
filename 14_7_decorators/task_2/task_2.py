from typing import Callable, Any
from functools import wraps
from time import sleep


def slowdown_2s(func: Callable) -> Callable:
    """Декоратор, который замедляет выполнение декорируемой функции на 2 секунды."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        sleep(2)
        result = func(*args, **kwargs)
        return result
    return wrapper
