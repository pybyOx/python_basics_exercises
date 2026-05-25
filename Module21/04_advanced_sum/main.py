def upgrade_sum(*args):
    total = 0
    for elem in args:
        if isinstance(elem, (int, float)):
            total += elem
        elif isinstance(elem, (list, tuple)):
            total += upgrade_sum(*elem)

    return total

# print(upgrade_sum([[1, 2, [3]], [1], 3]))
# print(upgrade_sum((1, 2, 3, 4, 5)))
