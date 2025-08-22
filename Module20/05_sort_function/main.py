def tpl_sort(my_tpl):
    for i in my_tpl:
        if not isinstance(i, int):
            return my_tpl
        else:
            return sorted(my_tpl)

# альтернативное решение
# def tpl_sort(my_tpl):
#     if ''.join(map(str, my_tpl)).replace('-', '').isdigit() and sum(my_tpl) % 1 == 0:
#         return sorted(my_tpl)
#     else:
#         return my_tpl


# tpl = (6, 3, -1, 8, 4, 10, -5)

# print(tpl_sort(tpl))

