def my_zip(*iterables):
    """Генератор, который повторяет поведение zip."""
    iterators = [iter(it) for it in iterables]
    while True:
        items = []
        for it in iterators:
            try:
                items.append(next(it))
            except StopIteration:
                return  # завершаем работу генератора
        yield tuple(items)


# Пример использования
user_string = 'abcd'
user_tpl = (10, 20, 30, 40)

gen = my_zip(user_string, user_tpl)
print(gen)  

for pair in gen:
    print(pair)
