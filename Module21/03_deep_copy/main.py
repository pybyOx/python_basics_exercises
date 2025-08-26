import copy

site = {
        'html': {
            'head': {
                'title': 'Куплю/продам {} недорого'
            },
            'body': {
                'h2': 'У нас самая низкая цена на {}',
                'div': 'Купить',
                'p': 'продать'
            }
        }
    }


def output(dictionary, indent=0):
    for key, value in dictionary.items():
        if isinstance(value, dict):
            print(" " * indent + f"{key}:")
            output(value, indent + 4)
        else:
            print(" " * indent + f"{key}: {value}")


def change_struct(my_struct: dict, name: str):
    for key, sub_struct in my_struct.items():
        if isinstance(sub_struct, str):
            my_struct[key] = sub_struct.replace('{}', name)
        else:
            change_struct(sub_struct, name)
    return my_struct


def create_new_struct(struct: dict, count: int):
    result = {}
    for _ in range(count):
        prod_name = input('\nВведите название продукта для нового сайта: ')
        new_struct = copy.deepcopy(struct)
        result[f'Сайт для {prod_name}'] = change_struct(new_struct, prod_name)
        for site_name, site_struct in result.items():
            print(f"\n{site_name}:")
            output(site_struct)
    return result


quantity = int(input('Сколько сайтов? '))
sites = create_new_struct(site, quantity)