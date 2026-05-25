from abc import ABC, abstractmethod


class Property(ABC):
    """Базовый класс для имущества.

    Attributes:
        _worth (float): Стоимость имущества.
    """
    def __init__(self, worth: float) -> None:
        """Инициализирует объект Property.

        Args:
            worth (float): Стоимость имущества.
        """
        self._worth = worth

    @abstractmethod
    def tax_calculation(self) -> float:
        """Рассчитывает налог для конкретного типа имущества.

        Returns:
            float: Сумма налога.
        """
        pass


class Apartment(Property):
    """Класс для квартиры. Налог = 1/1000 от стоимости."""

    def tax_calculation(self) -> float:
        """Вычисляет налог на квартиру.

        Returns:
            float: Налог на квартиру.
        """
        return self._worth / 1000


class Car(Property):
    """Класс для машины. Налог = 1/200 от стоимости."""

    def tax_calculation(self) -> float:
        """Вычисляет налог на машину.

        Returns:
            float: Налог на машину.
        """
        return self._worth / 200


class CountryHouse(Property):
    """Класс для дачи. Налог = 1/500 от стоимости."""

    def tax_calculation(self) -> float:
        """Вычисляет налог на дачу.

        Returns:
            float: Налог на дачу.
        """
        return self._worth / 500
