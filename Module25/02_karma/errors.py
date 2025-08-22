class KillError(Exception):
    def __init__(self):
        super().__init__('Убийство')


class DrunkError(Exception):
    def __init__(self):
        super().__init__('Пьянство')


class CarCrashError(Exception):
    def __init__(self):
        super().__init__('ДТП')


class GluttonyError(Exception):
    def __init__(self):
        super().__init__('Обжорство')


class DepressionError(Exception):
    def __init__(self):
        super().__init__('Уныние')
