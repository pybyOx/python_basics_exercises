def create_analysis_dictionary(alphabet='abcdefghijklmnopqrstuvwxyz'):
    analysis = dict()

    text_file = open('text.txt', 'r')
    symbols_list = [symbol for symbol in text_file.read().lower() if symbol in alphabet]
    text_file.close

    for symbol in set(symbols_list):
        analysis[symbol] = round(symbols_list.count(symbol) / len(symbols_list), 3)

    return dict(sorted(analysis.items(), key=lambda item: (-item[1], item[0])))


def write_result(dictionary):
    analysis_file = open('analysis.txt', 'w')
    for symbol, fraction in dictionary.items():
        analysis_file.write('{} {}\n'.format(symbol, fraction))
    analysis_file.close()


def read_file(file_name):
    my_file = open(file_name, 'r')
    print('\nСодержимое файла {}:\n{}'.format(file_name, my_file.read()))
    my_file.close()


write_result(create_analysis_dictionary())
read_file('text.txt')
read_file('analysis.txt')
