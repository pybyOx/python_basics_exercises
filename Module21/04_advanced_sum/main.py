def upgrade_sum(struct, total_sum=0):
    if isinstance(struct, tuple):
        struct = list(struct)
    for sub_struct in struct:
        if isinstance(sub_struct, int):
            total_sum += sub_struct
        else:
            total_sum = upgrade_sum(sub_struct, total_sum)
    return total_sum


# print(upgrade_sum([[1, 2, [3]], [1], 3]))
# print(upgrade_sum((1, 2, 3, 4, 5)))
