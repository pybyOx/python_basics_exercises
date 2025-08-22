def split_list(lst):
    less_lst, equals_lst, more_lst = [], [], []
    pivot = lst[-1]
    for digit in lst:
        if digit < pivot:
            less_lst.append(digit)
        elif digit == pivot:
            equals_lst.append(digit)
        else:
            more_lst.append(digit)

    return less_lst, equals_lst, more_lst


def qsort(my_list):
    less, equals, more = split_list(my_list)
    if len(less) > 1:
        less = qsort(less)
    if len(more) > 1:
        more = qsort(more)
    return less + equals + more


# numbers = [5, 8, 9, 4, 2, 9, 1, 8]
# print(qsort(numbers))
