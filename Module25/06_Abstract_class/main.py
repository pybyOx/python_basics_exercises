from math import pi
from abc import ABC, abstractmethod


class Shape(ABC):
    """Абстрактный базовый класс для геометрических фигур."""

    @abstractmethod
    def area(self) -> float:
        """Вычисляет площадь фигуры.

        Returns:
            float: Площадь фигуры.
        """
        pass


class Circle(Shape):
    """Класс, представляющий круг."""

    def __init__(self, radius: float) -> None:
        """Создает объект круга.

        Args:
            radius (float): Радиус круга.
        """
        self.radius: float = radius

    def area(self) -> float:
        """Вычисляет площадь круга.

        Returns:
            float: Площадь круга.
        """
        return pi * self.radius ** 2


class Rectangle(Shape):
    """Класс, представляющий прямоугольник."""

    def __init__(self, length: float, width: float) -> None:
        """Создает объект прямоугольника.

        Args:
            length (float): Длина прямоугольника.
            width (float): Ширина прямоугольника.
        """
        self.length: float = length
        self.width: float = width

    def area(self) -> float:
        """Вычисляет площадь прямоугольника.

        Returns:
            float: Площадь прямоугольника.
        """
        return self.length * self.width


class Triangle(Shape):
    """Класс, представляющий треугольник."""

    def __init__(self, base: float, height: float) -> None:
        """Создает объект треугольника.

        Args:
            base (float): Основание треугольника.
            height (float): Высота треугольника.
        """
        self.base: float = base
        self.height: float = height

    def area(self) -> float:
        """Вычисляет площадь треугольника.

        Returns:
            float: Площадь треугольника.
        """
        return 0.5 * self.base * self.height


# Примеры работы с классами
if __name__ == "__main__":
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 8)

    print("Площадь круга:", round(circle.area(), 2))
    print("Площадь прямоугольника:", rectangle.area())
    print("Площадь треугольника:", triangle.area())
