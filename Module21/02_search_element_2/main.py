def find_value(struct, key, deep=None):
    if key in struct:
        return struct[key]
    if deep:
        deep -= 1
        if deep == 0:
            return None
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            value = find_value(sub_struct, key, deep)
            if value:
                return value
    return None


site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

user_key = input('Введите искомый ключ: ')
user_deep = input('Хотите ввести максимальную глубину? Y/N:').lower()
if user_deep == 'y':
    max_deep = int(input('Введите максимальную глубину: '))
    result = find_value(site, user_key, max_deep)
else:
    result = find_value(site, user_key)
print('Значение ключа:', end=' ')
if result:
    print(result)
else:
    print('Такого ключа нет.')
