def output_dictionary(dictionary):
    for keys in sorted(dictionary.keys()):
        print('{}:{}'.format(keys, dictionary[keys]))


def invert_dictionary(dictionary):
    invert_dict = dict()
    for number in range(1, max(dictionary.values()) + 1):
        invert_dict[number] = [symbol for symbol in dictionary.keys() if dictionary[symbol] == number]
    return invert_dict


def histogram(string):
    symbols = dict()
    for symbol in string:
        if symbol in symbols:
            symbols[symbol] += 1
        else:
            symbols[symbol] = 1
    return symbols


text = input('Введите текст: ').lower()

frequency_dictionary = histogram(text)

invert_frequency_dictionary = invert_dictionary(frequency_dictionary)

print('\nОригинальный словарь частот:')
output_dictionary(frequency_dictionary)

print('\nИнвертированный словарь частот:')
output_dictionary(invert_frequency_dictionary)
