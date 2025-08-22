def split_list(lst):
    return ([elem for elem in lst if elem < lst[-1]],
            [elem for elem in lst if elem == lst[-1]],
            [elem for elem in lst if elem > lst[-1]])


def qsort(my_list):
    less, equals, more = split_list(my_list)
    if len(less) > 1:
        less = qsort(less)
    if len(more) > 1:
        more = qsort(more)
    return less + equals + more


# numbers = [5, 8, 9, 4, 2, 9, 1, 8]
# print(qsort(numbers))
