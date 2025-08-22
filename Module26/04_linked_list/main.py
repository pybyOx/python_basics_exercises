from typing import Optional, Any
from collections.abc import Iterable


class Node:

    """
    Класс, описывающий узел связного списка

    Args:
            info(Optional[Any]): Передаются данные, которые будет хранить узел.
    """

    def __init__(self, info: Optional[Any]) -> None:
        """
        Инициализирует узел связного списка.

        Args:
            info: Данные, которые будет хранить узел.
        """
        self.__info = info  # Данные, которые хранит узел
        self.__next = None  # Ссылка на следующий узел

    def get_info(self) -> Optional[Any]:
        """
        Геттер для получения информации узла

        :return:__info
        """
        return self.__info

    def get_next(self) -> Optional['Node']:
        """
        Геттер для получения ссылки на следующий узел

        :return: __next
        """
        return self.__next

    def set_next(self, new_value: Optional['Node']) -> None:
        """
        Сеттер для изменения ссылки на следующий узел
        :param new_value: новый узел
        :return: None
        """
        self.__next = new_value


class LinkedList:
    """
    Базовый класс, описывающий односвязный список
    """
    def __init__(self) -> None:
        """Инициализирует пустой связный список."""
        self.__head = None  # Начало списка
        self.__last = None  # Последний добавленный элемент

    def get_head(self) -> Optional['Node']:
        """
        Геттер для получения первого элемента в списке
        :return: __head
        """
        return self.__head

    def get_last(self) -> Optional['Node']:
        """
        Геттер для получения последнего добавленного элемента в списке
        :return: __last
        """
        return self.__last

    def set_head(self, new_value: Optional['Node']) -> None:
        """
        Сеттер для изменения первого элемента списка
        :param new_value: новый первый элемент
        :return: None
        """
        self.__head = new_value

    def set_last(self, new_value: Optional['Node']) -> None:
        """
        Сеттер для изменения последнего элемента списка
        :param new_value: новый последний элемент
        :return: None
        """
        self.__last = new_value

    def append(self, info: Optional[Any]) -> None:
        """
        Добавляет элемент в конец списка.
        Args:
            info: Данные, которые нужно добавить в список.
        """
        new_node = Node(info)

        if self.is_empty():
            self.set_head(new_node)
            self.set_last(new_node)
            return

        self.get_last().set_next(new_node)
        self.set_last(new_node)

    def get(self, index: int) -> Optional[Any]:
        """Получает элемент по индексу.

        Args:
            index: Индекс элемента, который нужно получить.

        Returns:
            Данные узла по заданному индексу.

        Raises:
            IndexError: Если индекс выходит за границы списка или список пуст.
        """
        if self.is_empty():
            raise IndexError('Элемент не может быть найден, так как список пуст.')

        return self.find_element(index).get_info()

    def remove(self, index: int) -> None:
        """Удаляет элемент по индексу.

        Args:
            index: Индекс элемента, который нужно удалить.

        Raises:
            IndexError: Если индекс выходит за границы списка или список пуст.
        """
        if self.is_empty():
            raise IndexError('Элемент не может быть удален, так как список пуст.')

        current = self.find_element(index)

        if current == self.get_head():
            self.set_head(self.get_head().get_next())
            if self.get_head() is None:
                self.set_last(None)
            return

        previous = self.get_head()
        while True:
            if previous.get_next() == current:
                previous.set_next(current.get_next())
                if previous.get_next() is None:
                    self.set_last(previous)
                break
            previous = previous.get_next()

    def __iter__(self) -> Iterable[Optional[Any]]:
        """Позволяет итерироваться по элементам списка.

        Yields:
            Данные каждого узла в списке.
        """
        current_node = self.get_head()

        while current_node:
            yield current_node.get_info()
            current_node = current_node.get_next()

    def find_element(self, index: int) -> Node:
        """Находит узел по индексу.

        Args:
            index: Индекс элемента, который нужно найти.

        Returns:
            Узел с данными по заданному индексу.

        Raises:
            IndexError: Если индекс выходит за границы списка.
        """
        current_node = self.get_head()

        for _ in range(index):
            if current_node is None:
                raise IndexError('Элемента с данным индексом в списке нет.')
            current_node = current_node.get_next()

        return current_node

    def is_empty(self) -> bool:
        """Проверяет, пуст ли связный список.

        Returns:
            bool: True, если список пуст, иначе False.
        """
        return self.get_head() is None

    def __str__(self) -> str:
        """Возвращает строковое представление связного списка.

        Returns:
            str: Строковое представление списка в формате '[info1, info2, ...]'.
        """
        return '[' + ', '.join(str(info) for info in self) + ']'


# Пример использования класса LinkedList
my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
