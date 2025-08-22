class KillError(Exception):
    def __str__(self):
        return 'Убийство'


class DrunkError(Exception):
    def __str__(self):
        return 'Пьянство'


class CarCrashError(Exception):
    def __str__(self):
        return 'ДТП'


class GluttonyError(Exception):
    def __str__(self):
        return 'Обжорство'


class DepressionError(Exception):
    def __str__(self):
        return 'Уныние'
