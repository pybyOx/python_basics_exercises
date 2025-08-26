def split_list(lst):
    pivot = lst[-1]
    less, equals, more = [], [], []
    for digit in lst:
        if digit < pivot:
            less.append(digit)
        elif digit == pivot:
            equals.append(digit)
        else:
            more.append(digit)
    return less, equals, more


def qsort(my_list):
    if len(my_list) <= 1:  
        return my_list
    less, equals, more = split_list(my_list)
    return qsort(less) + equals + qsort(more)


numbers = [5, 8, 9, 4, 2, 9, 1, 8]
print(qsort(numbers))
