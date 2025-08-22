def merge_sorted_lists(first_list, second_list):

    for number in first_list:
        for digit in second_list:
            if number == digit:
                second_list.remove(digit)
    first_list.extend(second_list)

    for index_1 in range(len(first_list)):
        minimal = index_1
        for index_2 in range(index_1, len(first_list)):
            if first_list[minimal] > first_list[index_2]:
                minimal = index_2
        first_list[minimal], first_list[index_1] = first_list[index_1], first_list[minimal]

    return first_list


list_1 = [1, 3, 5, 7, 9]
list_2 = [2, 4, 5, 6, 8, 10]

merged = merge_sorted_lists(list_1, list_2)

print(merged)
