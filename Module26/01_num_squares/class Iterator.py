from main import get_number
from typing import Self


class Iterator:
    def __init__(self, max_number: int) -> None:
        self.__maximum = max_number
        self.__minimum = 0

    def get_maximum(self) -> int:
        return self.__maximum

    def get_minimum(self) -> int:
        return self.__minimum

    def set_minimum(self, new_value: int) -> None:
        self.__minimum = new_value

    def __iter__(self) -> Self:
        self.set_minimum(0)
        return self

    def __next__(self) -> int:
        if self.get_minimum() < self.get_maximum():
            self.set_minimum(self.get_minimum() + 1)
            return self.get_minimum() ** 2
        else:
            raise StopIteration


maximum = get_number()
iterator = Iterator(maximum)
for number in iterator:
    print(number, end=' ')
