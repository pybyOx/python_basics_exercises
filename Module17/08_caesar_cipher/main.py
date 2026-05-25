alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
length = len(alphabet)


def new_index(old_index: int, shift: int) -> int:
    return (old_index + shift) % length


def encryption(text, shift):
    new_text = ''
    for symbol in text:
        if symbol.lower() in alphabet:
            new_char = alphabet[new_index(alphabet.index(symbol.lower()), shift)]
            new_text += new_char if symbol.islower() else new_char.upper()
        else:
            new_text += symbol
    return new_text


print('Зашифрованное сообщение:', encryption(text=input('Введите сообщение: '),
                                             shift=int(input('Введите сдвиг: '))))
