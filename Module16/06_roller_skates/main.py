def count_shoed_man(skates, man):
    score = 0
    for size_1 in skates:
        for size_2 in man:
            if size_1 == size_2:
                score += 1
                break
    return score


def create_list(my_list, amt):
    for score in range(amt):
        print('Размер', score + 1, ':', end=' ')
        size = int(input())
        my_list.append(size)


skates_amt = int(input('Кол-во коньков: '))
size_skates = []
create_list(size_skates, skates_amt)

man_amt = int(input('\nКол-во людей: '))
size_man = []
create_list(size_man, man_amt)

count = count_shoed_man(size_skates, size_man)

print('\nНаибольшее кол-во людей, которые могут взять ролики:', count)
