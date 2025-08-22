import re


def filter_numbers(my_list: list) -> None:
    """Функция, фильтрующая список номеров на соответствие требованиям"""
    for value in my_list:
        result = re.search(r'\b[89]\d{9}', value)
        print('Номер {}:'.format(value), end=' ')
        if result is not None:
            print('подходит')
        else:
            print('не подходит')


if __name__ == '__main__':

    numbers = ['9999999999', '999999-999', '99999x9999']

    filter_numbers(my_list=numbers)
