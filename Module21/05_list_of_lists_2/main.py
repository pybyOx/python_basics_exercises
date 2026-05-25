def open_list(my_list):
    result = []
    for elem in my_list:
        if isinstance(elem, list):
            result.extend(open_list(elem))
        else:
            result.append(elem)
    return result

# альтернативная функция через генератор

# def open_list(my_list):
#     for elem in my_list:
#         if isinstance(elem, list):
#             yield from open_list(elem)  # рекурсивный генератор
#         else:
#             yield elem


nice_list = [1,
             2,
             [3, 4],
             [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(f'Ответ: {open_list(nice_list)}')
