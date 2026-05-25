class MyDict(dict):
    """
    Собственный словарь, который работает как обычный dict,
    но метод get возвращает 0 по умолчанию вместо None.
    """
    def get(self, key, default=0):
        """
        Возвращает значение по ключу.
        Если ключ отсутствует, то возвращает 0 (или переданный default).
        """
        return super().get(key, default)


# Пример использования:
my_dict = MyDict(a=1, b=2)

print(my_dict.get("a"))       # 1
print(my_dict.get("c"))       # 0
print(my_dict.get("c", -1))   # -1 (переданный default имеет приоритет)
