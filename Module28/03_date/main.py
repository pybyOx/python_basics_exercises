from typing import Optional
from datetime import date


class Date:
    """
    Базовый класс, конвертирующий строку даты формата "dd-mm-yyyy"
    в объект класса Date, состоящий из соответствующих числовых значений дня, месяца и года.
    Args:
        day(int): передается день
        month(int): передается месяц
        year(int): передается год
    """
    def __init__(self, day: int, month: int, year: int) -> None:
        """Инициализирует объект класса Date."""
        self._day = day
        self._month = month
        self._year = year

    @property
    def day(self) -> int:
        """Геттер, возвращающий день месяца"""
        return self._day

    @day.setter
    def day(self, value: int) -> None:
        """Сеттер, устанавливающий день месяца"""
        self._day = value

    @property
    def month(self) -> int:
        """Геттер, возвращающий числовое значение месяца"""
        return self._month

    @month.setter
    def month(self, value: int) -> None:
        """Сеттер, устанавливающий числовое значение месяца"""
        self._month = value

    @property
    def year(self) -> int:
        """Геттер, возвращающий год"""
        return self._year

    @year.setter
    def year(self, value: int) -> None:
        """Сеттер, устанавливающий год"""
        self._year = value

    @classmethod
    def from_string(cls, date_string: str) -> Optional['Date']:
        """
        Создает объект Date из строки в формате 'dd-mm-yyyy'
        Args:
            date_string(str): Строка, представляющая дату в формате 'dd-mm-yyyy'
        Returns:
            Optional['Date']: Объект Date или None, если строка имеет неверный формат или дата некорректна.
        """
        day, month, year = map(int, date_string.split('-'))
        if cls.is_date_valid(date_string):
            return Date(day, month, year)
        else:
            print('Введена некорректная дата.')
            return None

    @classmethod
    def is_date_valid(cls, date_string: str) -> bool:
        """Метод, проверяющий корректность введенной даты.
        Args:
            date_string(str): Принимает дату формата ‘dd-mm-yyyy’
        Returns:
            bool: Возвращает True, если введена корректная дата.
        """
        try:
            day, month, year = map(int, date_string.split('-'))
            date(year, month, day)
            return True
        except ValueError:
            return False

    def __str__(self) -> str:
        """Возвращает строковое представление объекта Date"""
        return 'День: {}    Месяц: {}    Год: {}'.format(self.day, self.month, self.year)


my_date = Date.from_string('10-12-2077')
print(my_date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
