from main import get_number


sequence = (number ** 2 for number in range(1, get_number() + 1))
for value in sequence:
    print(value, end=' ')
