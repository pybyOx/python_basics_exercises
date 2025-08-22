def open_list(my_list):
    index = 0
    for struct in tuple(my_list):
        if isinstance(struct, int):
            index += 1
            my_list.append(struct)
        else:
            struct = open_list(struct)
            index += 1
            my_list += struct

    return my_list[index:]


nice_list = [1,
             2,
             [3, 4],
             [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print('Ответ: {}'.format(open_list(nice_list)))

# решила методом тыка, наверняка можно было проще ¯\_(о_О)_/¯
