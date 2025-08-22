from typing import Callable

callbacks = {}  # Словарь для хранения функций обратного вызова


def callback(path: str) -> Callable:
    """Декоратор для регистрации функции обратного вызова по указанному маршруту."""
    def decorator(func: Callable) -> Callable:
        callbacks[path] = func  # Если эту строку переместить в wrapped, ничего не получается. Почему?
        # Потому что wrapped вызывается только при выполнении самой функции, а регистрация функции
        # в словарь callback должна происходить на этапе декорирования, то есть когда Python листит @callback('//')

        def wrapped(*args, **kwargs):
            value = func(*args, **kwargs)
            return value
        return wrapped
    return decorator


@callback('//')
def example():
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = callbacks.get('//')

if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
