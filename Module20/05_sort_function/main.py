def tpl_sort(my_tpl):
    if not all(isinstance(element, int) for element in my_tpl):
        return my_tpl
    return tuple(sorted(my_tpl))


# tpl = (6, 3, -1, 8, 4, 10, -5)

# print(tpl_sort(tpl))
