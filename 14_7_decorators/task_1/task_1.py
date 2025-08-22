from typing import Callable, Any
from functools import wraps


def how_are_you(func: Callable) -> Callable:
    """Декоратор, который задаёт вопрос пользователю перед вызовом декорируемой функции."""
    @wraps(func)
    def wrapped_func(*args, **kwargs) -> Any:
        result = input('Как дела? ')
        print(f"У тебя {result}, а у меня не очень! Ладно, держи свою функцию.")
        result = func(*args, **kwargs)
        return result
    return wrapped_func


@how_are_you
def test():
    pass


test()
