def create_list(amt):
    my_list = []
    for score in range(amt):
        print('Число №', score + 1, ':', end=' ')
        number = int(input())
        my_list.append(number)
    return my_list


def symmetry_checking(my_list):
    subtrahend = 1
    amt = 0
    for index in range(len(my_list)//2 + 1):
        if my_list[index] == my_list[index - subtrahend]:
            subtrahend += 2
            amt += 1
    if amt == len(my_list)//2 + 1:
        return True
    else:
        return False


numbers_amt = int(input('Кол-во чисел: '))

numbers_list = create_list(numbers_amt)

print('Последовательность:', numbers_list)

symmetry = symmetry_checking(numbers_list)

if symmetry:
    print('Последовательность является симметричной')
else:
    asymmetrical_list = []

    while True:
        asymmetrical_list.append(numbers_list[0])
        numbers_list.remove(numbers_list[0])

        if symmetry_checking(numbers_list):
            print('Нужно приписать чисел:', len(asymmetrical_list))
            asymmetrical_list.reverse()
            print('Сами числа:', asymmetrical_list)
            break

        else:
            continue
