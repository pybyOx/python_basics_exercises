def create_dictionary():
    count_pair = int(input('Введите количество пар слов: '))
    dictionary_pair = dict()
    for digit in range(count_pair):
        print('{}-я пара:'.format(digit + 1))
        first_word, second_word = input('Слово: ').title(), input('Cиноним: ').title()
        dictionary_pair[first_word] = second_word
        dictionary_pair[second_word] = first_word

    return dictionary_pair


def check_dictionary(dictionary):
    while True:
        user_word = input('\nВведите слово: ').title()
        if user_word in dictionary.keys():
            print('Синоним: {}'.format(dictionary.get(user_word)))
            break
        else:
            print('Такого слова в словаре нет.')


pair_dictionary = create_dictionary()

check_dictionary(pair_dictionary)
