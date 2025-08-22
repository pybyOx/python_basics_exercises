from _collections_abc import Callable
from functools import wraps


def check_permission(user: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapped(*args, **kwargs):
            try:
                if user in user_permissions:
                    value = func(*args, **kwargs)
                    return value
                raise PermissionError('PermissionError')
            except PermissionError as error:
                print('{}: у пользователя недостаточно прав, чтобы выполнить функцию {}'.format(
                    error, func.__name__))
        return wrapped
    return decorator


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()

# Объясните, пожалуйста, почему переменная user_permissions доступна внутри декоратора,
# даже если мы ее не передали как аргумент?

# Почему-то я запомнила, что внутри функций свои локальные переменные и не пересекаются
# с переменными основного кода.
