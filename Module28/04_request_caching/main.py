from typing import Any, Optional, Tuple


class LRUCache:
    """
    Базовый класс, который хранит ограниченное
    количество объектов и, при превышении лимита, удаляет самые старые
    использованные элементы.
    Args:
        capacity (int): Максимальное количество элементов, которое может хранить кэш
    """

    def __init__(self, capacity: int) -> None:
        """Инициализирует объект класса LRUCache с заданной вместимостью."""
        self.capacity = capacity
        self.cache_dict = {}  # Словарь для хранения кэшированных элементов
        self.usage_queue = []  # Список для отслеживания порядка использования элементов

    def get(self, key: Any) -> Optional[Any]:
        """
        Возвращает значение элемента по ключу из кэша.
        Если элемент найден, он перемещается в конец очереди использования,
        чтобы указать, что он был использован недавно.
        Args:
            key: Ключ элемента, который нужно получить.
        Returns:
            Значение элемента по ключу, если он найден в кэше.
            None, если элемент не найден.
        """
        if key in self.cache_dict:
            self.usage_queue.remove(key)
            self.usage_queue.append(key)
            return self.cache_dict[key]
        return None

    @property
    def cache(self) -> Optional[Tuple]:
        """Возвращает самый старый элемент в кэше.
        Returns:
            tuple: Кортеж (ключ, значение) самого старого элемента.
                   None, если кэш пуст.
        """
        if self.usage_queue:
            oldest_key = self.usage_queue[0]
            return oldest_key, self.cache_dict[oldest_key]
        return None

    @cache.setter
    def cache(self, new_elem: tuple) -> None:
        """
        Добавляет новый элемент в кэш.
        Если кэш достиг максимальной вместимости, удаляет самый старый элемент
        перед добавлением нового.
        Args:
            new_elem (tuple): Кортеж (ключ, значение) нового элемента для добавления в кэш.
        """
        key, value = new_elem
        if key in self.cache_dict:
            self.usage_queue.remove(key)
            self.usage_queue.append(key)
            self.cache_dict[key] = value
        else:
            if len(self.cache_dict) >= self.capacity:
                oldest_key = self.usage_queue.pop(0)
                del self.cache_dict[oldest_key]

            self.cache_dict[key] = value
            self.usage_queue.append(key)

    def print_cache(self):
        """Выводит текущее содержимое кэша в формате "ключ: значение"."""
        print("LRU Cache:")
        for key in self.usage_queue:
            print('{} : {}'.format(key, self.cache_dict[key], end=', '))
        print()


# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

# # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3

# Получаем значение по ключу
print(cache.get("key2"))  # value2

# Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")

# Выводим обновленный кэш
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
