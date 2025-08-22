text = input('Введите строку: ')

text = text[text.index('h') + 1: text.rindex('h')]

print('Развёрнутая последовательность между первым и последним h:', text[::-1])
