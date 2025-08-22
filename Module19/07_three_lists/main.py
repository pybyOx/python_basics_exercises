def tasks_without(list_1, list_2, list_3):
    elements_repetitive = []
    non_repeating_elements = []
    for digit in list_1:
        if digit in list_2 and digit in list_3:
            elements_repetitive.append(digit)
        elif digit not in list_2 and digit not in list_3:
            non_repeating_elements.append(digit)
    return [elements_repetitive, non_repeating_elements]


def tasks_with(set_1, set_2, set_3):
    return [sorted(set_1 & (set_2 & set_3)), sorted(set_1 - (set_2 | set_3))]


def output(list_1, list_2, list_3):
    results_list = [tasks_without(list_1, list_2, list_3),
                    tasks_with(set(list_1), set(list_2), set(list_3))]
    for i, result in enumerate(results_list):
        print('\nЗадача {}:'
              '\nРешение без множеств: {}'
              '\nРешение с множествами: {}'
              .format(i + 1,
                      results_list[0][i],
                      results_list[1][i]))


array_1 = [1, 5, 10, 20, 40, 80, 100]

array_2 = [6, 7, 20, 80, 100]

array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

output(array_1, array_2, array_3)
