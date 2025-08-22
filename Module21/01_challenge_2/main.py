def make_range(maximum):
    if maximum == 0:
        return maximum
    make_range(maximum - 1)
    print(maximum)


number = int(input('Введите num: '))
make_range(number)
