from typing import Callable, Any, Optional


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """Декоратор для декораторов, позволяющий любому декоратору принимать произвольные аргументы."""
    def wrapped_decorator(*args, **kwargs):
        print("Переданные арги и кварги в декоратор:", args, kwargs)

        def actual_decorator(func: Callable) -> Callable:
            return decorator(func, *args, **kwargs)
        return actual_decorator
    return wrapped_decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args: Optional[Any], **kwargs: Optional[Any]) -> Callable:
    """Декоратор, который может принимать произвольные аргументы."""
    def wrapper(*args2, **kwargs2):
        return func(*args2, **kwargs2)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)

# Когда Python встречает @decorated_decorator(100, 'рублей', 200, 'друзей'), сначала эти аргументы передаются
# в decorator_with_args_for_any_decorator, а затем в decorated_decorator. Это параметры самого декоратора, они
# попадают в args и kwargs.
# Когда же вызывается decorated_function("Юзер", 101), аргументы передаются уже внутрь
# wrapper, и там они оказываются в args2 и kwargs2.
# Разделение происходит автоматически: сначала передаёте параметры декоратору, потом отдельно аргументы функции.
# Python просто обрабатывает их на разных уровнях вложенности.
