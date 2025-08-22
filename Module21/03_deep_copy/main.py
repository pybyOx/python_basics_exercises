import copy


def output(dictionary):
    for key, value in dictionary.items():
        if isinstance(value, str):
            print('    {}:{}'.format(key, value))
        else:
            print('{}:'.format(key))
            output(value)


def change_struct(my_struct, name):
    for key, sub_struct in my_struct.items():
        if isinstance(sub_struct, str):
            new_value = sub_struct.replace('{}', name)
            my_struct[key] = new_value
            return my_struct
        else:
            my_struct[key] = change_struct(sub_struct, name)
    return my_struct


def create_new_struct(struct, count, result):
    if count == 0:
        return None
    user_name = input('\nВведите название продукта для нового сайта: ')
    new_struct = copy.deepcopy(struct)
    result['Сайт для {}'.format(user_name)] = change_struct(new_struct, user_name)
    output(result)
    create_new_struct(struct, count - 1, result)


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


quantity = int(input('Сколько сайтов? '))
sites = dict()
create_new_struct(site, quantity, sites)
