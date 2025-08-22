def create_dictionary():
    count_pair = int(input('Введите количество пар слов: '))
    dictionary_pair = dict()
    for digit in range(count_pair):
        print('{}-я пара:'.format(digit + 1))
        synonym_1 = input('Введите слово: ').title()
        synonym_2 = input('Введите синоним к этому слову: ').title()
        dictionary_pair[synonym_1] = synonym_2
    return dictionary_pair


def check_dictionary(dictionary):
    while True:
        user_word = input('\nВведите слово: ').title()
        if user_word in dictionary.keys():
            print('Синоним: {}'.format(dictionary.get(user_word)))
            break
        elif user_word in dictionary.values():
            for key in dictionary.keys():
                if dictionary[key] == user_word:
                    print('Синоним: {}'.format(key))
                    break
            break
        else:
            print('Такого слова в словаре нет.')


pair_dictionary = create_dictionary()

check_dictionary(pair_dictionary)
