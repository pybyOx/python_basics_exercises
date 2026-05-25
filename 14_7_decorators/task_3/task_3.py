from datetime import datetime
from typing import Callable, Any
from functools import wraps


def logging(func: Callable) -> Callable:
    """Декоратор, отвечающий за логирование декорируемой функции."""
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:

        try:
            print('Имя функции: {}\nДокументация: {}'.format(func.__name__, func.__doc__))
            result = func(*args, **kwargs)
            return result
        except Exception as error:
            print('Возникла ошибка {}'.format(error))
            with open('function_errors.log', 'a', encoding='utf-8') as file:
                file.write('\n{time}: Ошибка - {error} в функции {func}'.format(time=datetime.now(),
                                                                                error=error,
                                                                                func=func.__name__))

    return wrapper
