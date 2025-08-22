nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

nice_list = [number for part_big in nice_list for part_small in part_big for number in part_small]

print(nice_list)
