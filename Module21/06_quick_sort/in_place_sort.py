# классическая реализация Хоара «на месте» (in-place)

def hoare_quick_sort(lst: list, low: int, high: int):
    if low < high:

        p = partition(lst, low, high)  # Разделяем список и получаем индекс опорного элемента

        # Рекурсивно сортируем левую и правую части
        hoare_quick_sort(lst, low, p)
        hoare_quick_sort(lst, p + 1, high)


def partition(lst: list, low: int, high: int):
    pivot = lst[(low + high) // 2]  # pivot — середина списка
    i, j = low, high
    while True:

        while lst[i] < pivot:  # Сдвигаем левый указатель вправо, пока элемент меньше pivot
            i += 1

        while lst[j] > pivot:  # Сдвигаем правый указатель влево, пока элемент больше pivot
            j -= 1

        if i >= j:
            return j  # возвращаем точку разделения

        lst[i], lst[j] = lst[j], lst[i]  # Меняем элементы местами
        i += 1
        j -= 1


# Пример использования:
numbers = [5, 8, 9, 4, 2, 9, 1, 8]
print("До сортировки:", numbers)
hoare_quick_sort(numbers, 0, len(numbers) - 1)
print("После сортировки:", numbers)
