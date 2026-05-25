synonyms = {}
for i in range(int(input('Введите количество пар слов: '))):
    while True:
        words = input(f'{i+1}-я пара: ')
        pair = [word.strip().lower() for word in words.split() if word.isalpha()]
        if len(pair) == 2:
            word1, word2 = pair[0], pair[1]
            synonyms[word1], synonyms[word2] = word2, word1
            break
        print('Некорректный ввод. \nВведите два слова-синонима')

# поиск синонимов
while True:
    user_word = input('\nВведите слово: ').strip().lower()
    if user_word in synonyms:
        print(f'Синоним: {synonyms[user_word].title()}')
        break
    else:
        print('Такого слова в словаре нет.')
