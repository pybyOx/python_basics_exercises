def check_palindrome(string):
    if string == string[::-1]:
        return True
    else:
        return False


def check_possible(string):
    count = 0
    for symbol in set(string):
        if string.count(symbol) % 2 != 0:
            count += 1
    if count > 1:
        print('Нельзя сделать палиндромом')
    else:
        print('Можно сделать палиндромом')


text = input('Введите строку: ')

if check_palindrome(text):
    print('Строка является палиндромом!')
else:
    check_possible(text)
