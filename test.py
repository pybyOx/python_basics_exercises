numbers = input('Введите строку: ')
print(list(filter(lambda elem: False if elem.isdigit or elem.upper else True, numbers.split(' '))))
