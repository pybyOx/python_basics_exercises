def is_prime(number):
    if number <= 1:
        return False
    for divider in range(2, int(number ** 0.5) + 1):
        if number % divider == 0:
            return False
    return True


def crypto(iterable):
    return [value for index, value in enumerate(iterable) if is_prime(index)]


print(crypto('О Дивный Новый мир!'))
