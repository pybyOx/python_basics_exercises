class Stack:

    def __init__(self):
        self.__my_stack = []

    def get_stack(self):
        return self.__my_stack

    def add_element(self, element):
        self.get_stack().insert(0, element)

    def delete_element(self, element):
        while element in self.get_stack():
            self.get_stack().remove(element)


class TaskManager:
    def __init__(self):
        self.__my_tacks = dict()

    def __str__(self):
        return '\n'.join([f'{key} - {', '.join(value)}' for key, value in self.get_tasks().items()])

    def get_tasks(self):
        return self.__my_tacks

    def set_tasks(self, new_dict):
        self.__my_tacks = new_dict

    def new_task(self, task, priority):
        if priority in self.get_tasks().keys():
            self.get_tasks()[priority].append(task)
        else:
            self.get_tasks()[priority] = [task]

        # после добавления задачи сортируем стек по приоритетности
        self.set_tasks({key: self.get_tasks()[key] for key in sorted(self.get_tasks().keys())})

    def delete_task(self, task, priority=None):
        if priority is None:  # задача удаляется из всего стека
            for task_list in self.get_tasks().values():
                while task in task_list:
                    task_list.remove(task)
        else:  # задача удаляется из указанного приоритета
            while task in self.get_tasks()[priority]:
                self.get_tasks()[priority].remove(task)
