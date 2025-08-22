import json
from typing import Dict, List, Any
from pprint import pprint


def data_comparison(old: Dict[str, Any], new: Dict[str, Any], check_list: List[str]) -> Dict[str, Any]:
    """Сравнивает два словаря по указанным ключам.
    Args:
        old: Словарь со старыми данными
        new: Словарь с новыми данными
        check_list: Ключи для сравнения
    Returns:
        Словарь с различиями {ключ: новое_значение}
    """

    return {key: new[key] for key in check_list if old.get(key) != new.get(key)}


def filter_data(data: Dict[str, Any], check_list: List[str]) -> Dict[str, Any]:
    """Рекурсивно фильтрует данные, оставляя только указанные ключи во всех уровнях вложенности.
    Args:
        data: Исходный словарь для фильтрации
        check_list: Список ключей для сохранения
    Returns:
        Словарь только с целевыми ключами и их значениями
    """
    filtered_dict = {}

    def dict_read(my_dict: Dict[str, Any]) -> None:
        for key, value in my_dict.items():
            if key in check_list:
                filtered_dict[key] = value
            elif isinstance(value, dict):
                dict_read(value)
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        dict_read(item)

    dict_read(data)
    return filtered_dict


if __name__ == '__main__':

    diff_list = ["services", "staff", "datetime"]

    with open('json_old.json', encoding='utf-8') as file:
        old_data = json.load(file)

    with open('json_new.json', encoding='utf-8') as file:
        new_data = json.load(file)

    filtered_old = filter_data(old_data, diff_list)
    filtered_new = filter_data(new_data, diff_list)

    if filtered_old and filtered_new:
        result = data_comparison(filtered_old, filtered_new, diff_list)

        print('Словарь с измененными значениями:')
        pprint(result, sort_dicts=False)

        with open('result.json', 'w') as file:
            json.dump(result, file, indent=4)
