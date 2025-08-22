def encryption(text, shift):

    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    text = [alphabet[alphabet.index(symbol) - len(alphabet) + shift]
            if symbol in alphabet
            else ' '
            for symbol in text]

    return ''.join(text)


my_text = input('Введите сообщение: ')
my_shift = int(input('Введите сдвиг: '))

print('Зашифрованное сообщение:', encryption(my_text, my_shift))
