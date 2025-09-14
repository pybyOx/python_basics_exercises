from random import choice


class KarmaError(Exception):
    """Базовое исключение для ошибок кармы."""

    def __init__(self, message: str):
        super().__init__(message)

    @classmethod
    def random_error(cls):
        """Возвращает случайный экземпляр одного из дочерних классов KarmaError."""
        return choice(cls.__subclasses__())()


class KillError(KarmaError):
    """Ошибка: Убийство."""
    def __init__(self):
        super().__init__('Убийство')


class DrunkError(KarmaError):
    """Ошибка: Пьянство."""
    def __init__(self):
        super().__init__('Пьянство')


class CarCrashError(KarmaError):
    """Ошибка: ДТП."""
    def __init__(self):
        super().__init__('ДТП')


class GluttonyError(KarmaError):
    """Ошибка: Обжорство."""
    def __init__(self):
        super().__init__('Обжорство')


class DepressionError(KarmaError):
    """Ошибка: Уныние."""
    def __init__(self):
        super().__init__('Уныние')
