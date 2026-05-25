def output_dictionary(my_dict):
    for key in sorted(my_dict.keys()):
        print(f'{key}:{my_dict[key]}')


text = input('Введите текст: ').lower()

dictionary = {symbol: text.count(symbol) for symbol in set(text)}

# from collections import Counter
# dictionary = Counter(text)

invert_dictionary = {number: [symbol for symbol in dictionary.keys() if dictionary[symbol] == number]
                     for number in range(1, max(dictionary.values()) + 1)}

# invert_dictionary = {}
# for symbol, count in dictionary.items():
#     invert_dictionary.setdefault(count, []).append(symbol)

print('\nОригинальный словарь частот:')
output_dictionary(dictionary)

print('\nИнвертированный словарь частот:')
output_dictionary(invert_dictionary)
