# Реализуйте декоратор logging, который будет отвечать за логирование функций.
# На экран выводится название функции и её документация. Если во время выполнения декорируемой функции возникла
# ошибка, то в файл function_errors.log записывается название функции и ошибки.
#
# Постарайтесь сделать так, чтобы программа не завершалась после обнаружения первой же ошибки,
# а обрабатывала все декорируемые функции и сразу записывала все ошибки в файл.
#
# Дополнительно: запишите дату и время возникновения ошибки, используя модуль datetime.

from datetime import datetime
from typing import Callable, Any
from functools import wraps


def logging(func: Callable) -> Callable:
    """
    Декоратор, отвечающий за логирование декорируемой функции.
    :param func: Функция, которую нужно декорировать.
    :return: Ссылка на функцию-обёртку.
    """
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        """
        Обертка для декорируемой функции, выводящая ее название и документацию.
        При возникновении ошибки, записывает название функции и ошибки в файл function_errors.log.
        :param args: Позиционные аргументы, передаваемые в декорируемую функцию.
        :param kwargs:Именованные аргументы, передаваемые в декорируемую функцию.
        :returns Результат, возвращаемый декорируемой функцией.
        """
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
