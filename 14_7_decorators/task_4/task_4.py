from functools import wraps
from typing import Callable


def cache_decorator(func: Callable) -> Callable:
    """Декоратор для кеширования результатов выполнения функции,
    которая принимает одно целое число и возвращает целое число."""
    cache = dict()

    @wraps(func)
    def wrapper(number: int) -> int:
        """Обёртка для кешируемой функции, осуществляющая хранение результатов.
        Args:
            number: Целое число, для которого необходимо получить результат.
        Returns: Результат выполнения функции.
                 Если функция уже вызывалась с данным аргументом, результат берётся из кеша.
        """
        if number not in cache:
            cache[number] = func(number)
        return cache[number]
    return wrapper


@cache_decorator
def fibonacci(number):
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован

# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
