text = input('Введите текст: ')

text = [letter for letter in text if letter in 'АаУуОоИиЭэЫыЯяЮюЕеЁё']

print('Список гласных букв:', text, '\nДлина списка:', len(text))
