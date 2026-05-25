from errors import KarmaError
from random import randint

CONSTANT = 500


def one_day() -> int:
    """Симулирует один прожитый день.

    С вероятностью 1/10 выбрасывает случайное исключение из KarmaError.
    В остальных случаях возвращает количество кармы от 1 до 7.

    Returns:
        int:количество очков кармы (от 1 до 7), если день прошёл без происшествий.

    Raises:
        KillError: если случайным образом произошла ошибка убийства.
        DrunkError: если случайным образом произошла ошибка пьянства.
        CarCrashError: если случайным образом произошла ошибка ДТП.
        GluttonyError: если случайным образом произошла ошибка обжорства.
        DepressionError: если случайным образом произошла ошибка уныния.
    """
    if randint(1, 10) == 1:
        raise KarmaError.random_error()
    return randint(1, 7)


with open('karma.log', 'w', encoding="utf-8") as log_file:
    karma = 0
    day_count = 1
    while karma < CONSTANT:
        print(f'\nДень {day_count}')
        try:
            day_karma = one_day()
            print(f'+{day_karma} к карме')
            karma += day_karma

        except KarmaError as error:
            print(error)
            log_file.write(f'День {day_count} : {str(error)} \n')

        day_count += 1

    print('\nКарма достигла константы.')
