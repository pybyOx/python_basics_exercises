from main import get_number


def generator(maximum: int) -> int:
    for number in range(1, maximum + 1):
        yield number ** 2


sequence = generator(maximum=get_number())
for value in sequence:
    print(value, end=' ')
