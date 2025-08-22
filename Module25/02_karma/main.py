from errors import KillError, DrunkError, CarCrashError, GluttonyError, DepressionError
from random import randint, choice

error_list = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]


def one_day():
    if randint(1, 10) == 1:
        error_choice = choice(error_list)
        return error_choice()
    else:
        return randint(1, 7)


with open('karma.log', 'w', encoding="utf-8") as log_file:
    constant = 500
    karma = 0
    day_count = 1
    while karma < constant:
        print('\nДень {}'.format(day_count))
        try:
            day_karma = one_day()
            if isinstance(day_karma, int):
                print('+{} к карме'.format(day_karma))
                karma += day_karma
            else:
                raise day_karma

        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as error:
            print(error)
            log_file.write('День {} : {} \n'.format(day_count, error.__str__()))

        day_count += 1

    print('\nКарма достигла константы.')
