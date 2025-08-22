import requests
import json
import pprint
from typing import Optional, Dict


def link_to_dict(my_link: str) -> Optional[Dict]:
    """Десериализует JSON из URL.
    :param my_link: Ссылка на ресурс.
    :return: Словарь с данными из ресурса или None.
    :raises ConnectionError: Если ресурс не найден или запрос завершился с ошибкой.
    """
    try:
        response = requests.get(my_link)
        if response.status_code != 200:
            raise ConnectionError('Запрошенный ресурс не найден.')
        return json.loads(response.text)
    except ConnectionError as error:
        print('Произошла ошибка запроса:', error)
        return None


def filter_info(high_dict: dict) -> dict:
    """Фильтрует словарь, оставляя только необходимые ключи.
    :param high_dict: Исходный словарь.
    :return: Словарь с отфильтрованными данными.
    """
    low_dict = {}

    def filter_dict(my_dict: dict, result: dict) -> dict:
        for key, value in my_dict.items():
            if isinstance(value, dict):
                filter_dict(value, result)
            if key in ["name", "max_atmosphering_speed", "starship_class",
                       "height", "mass", "pilots", "homeworld"]:
                result[key] = value
        return result

    return filter_dict(high_dict, low_dict)


if __name__ == '__main__':

    # получаем информацию о корабле
    ship_url = 'https://www.swapi.tech/api//starships/12'
    ship_info = filter_info(link_to_dict(ship_url))

    # получаем информацию о пилотах корабля
    pilots_info = []
    for pilot_link in ship_info['pilots']:
        pilot_info = filter_info(link_to_dict(pilot_link))
        if pilot_info:
            pilot_info['homeworld_name'] = filter_info(link_to_dict(pilot_info['homeworld']))['name']
            pilots_info.append(pilot_info)

    # объединяем информацию
    ship_info['pilots'] = pilots_info

    # записываем в json-файл
    with open('ship_info.json', 'w') as file:
        json.dump(ship_info, file, indent=4)

    print('\n\t\tИнформация о корабле X-wing:')
    print('-'*65)
    pprint.pprint(ship_info, sort_dicts=False)
