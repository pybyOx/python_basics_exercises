from typing import Optional, Any


class Stack:
    """Класс реализует структуру данных 'стек' (LIFO)."""

    def __init__(self):
        self.__stack: list = []

    def push(self, element: Any) -> None:
        """Добавляет элемент наверх стека"""
        self.__stack.append(element)

    def pop(self) -> Optional[Any]:
        """Удаляет и возвращает верхний элемент стека. Если стек пуст — возвращает None."""
        if self.__stack:
            return self.__stack.pop()
        return None

    def peek(self) -> Optional[Any]:
        """Возвращает верхний элемент стека без удаления. Если стек пуст — возвращает None."""
        if self.__stack:
            return self.__stack[-1]
        return None

    def is_empty(self) -> bool:
        """Проверяет, пуст ли стек."""
        return len(self.__stack) == 0

    def __len__(self) -> int:
        """Возвращает количество элементов в стеке."""
        return len(self.__stack)

    def __str__(self) -> str:
        return f"Stack: {self.__stack}"


class TaskManager:
    """
    Класс для управления задачами по приоритету.

    Задачи хранятся в виде словаря:
    {
        priority (int): [task1 (str), task2 (str), ...]
    }
    """
    def __init__(self):
        self.__tasks: dict[int, list[str]] = {}

    @property
    def tasks(self) -> dict[int, list[str]]:
        """Возвращает словарь задач по приоритетам."""
        return self.__tasks

    @tasks.setter
    def tasks(self, new_dict: dict[int, list[str]]) -> None:
        """
        Устанавливает новый словарь задач с сортировкой по приоритетам.
        Чем меньше число — тем выше приоритет.
        """
        self.__tasks = {k: new_dict[k] for k in sorted(new_dict)}

    def new_task(self, task: str, priority: int) -> None:
        """Добавляет новую задачу с заданным приоритетом"""
        if priority in self.tasks:
            self.tasks[priority].append(task)
        else:
            self.tasks[priority] = [task]

        # пересортируем через сеттер
        self.tasks = self.tasks

    def delete_task(self, task: str, priority: int | None = None) -> None:
        """
       Удаляет задачу по приоритету или из всех приоритетов.
       Если указать priority=None — задача удаляется из всех списков.
       """
        if priority is None:
            for task_list in self.tasks.values():
                while task in task_list:
                    task_list.remove(task)
        else:
            if priority in self.tasks:
                while task in self.tasks[priority]:
                    self.tasks[priority].remove(task)

    def __str__(self) -> str:
        """Возвращает строковое представление задач, отсортированных по приоритетам."""
        return "\n".join(f"{priority} {'; '.join(tasks)}"
                         for priority, tasks in self.__tasks.items())
