from collections import Counter


def can_be_poly(text: str) -> bool:
    return len(text) % 2 == sum(map(lambda elem: elem % 2, Counter(text).values()))


if __name__ == '__main__':
    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))
