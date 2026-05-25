def count_shoed_man(skates, man):
    count = 0
    for s_skate in skates:
        for s_man in man:
            if s_skate == s_man:
                count += 1
                man.remove(s_man)
                break
    return count


size_skates = [int(input(f'Размер {i + 1}-й пары: ')) for i in range(int(input('Кол-во коньков: ')))]

size_man = [int(input(f'Размер ноги {i + 1}-го человека: ')) for i in range(int(input('\nКол-во людей: ')))]

print('\nНаибольшее кол-во людей, которые могут взять ролики:', count_shoed_man(size_skates, size_man))
