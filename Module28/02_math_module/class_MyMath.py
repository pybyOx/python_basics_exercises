from typing import Union


class MyMath:
    """Базовый класс, выполняющий математические вычисления, связанные с фигурами."""
    @staticmethod
    def circle_len(cls, radius: Union[int, float]) -> Union[int, float]:
        """Метод, вычисляющий длину окружности.
        Args:
            radius(Union[int, float]): Принимает радиус окружности.
        Returns:
            Union[int, float]: Возвращает длину окружности.
        """
        return 2 * 3.14 * radius

    @staticmethod
    def circle_sq(cls, radius: Union[int, float]) -> Union[int, float]:
        """Метод, вычисляющий площадь окружности.
        Args:
            radius(Union[int, float]): Принимает радиус окружности.
        Returns:
            Union[int, float]: Возвращает площадь окружности.
        """
        return 3.14 * radius ** 2

    @staticmethod
    def cube_volume(cls, edge: Union[int, float]) -> Union[int, float]:
        """Метод, вычисляющий объем куба.
        Args:
            edge(Union[int, float]): Принимает ребро куба.
        Returns:
            Union[int, float]: Возвращает объем куба.
        """
        return edge ** 3

    @staticmethod
    def sphere_surface_sq(cls, radius: Union[int, float]) -> Union[int, float]:
        """Метод, вычисляющий площадь поверхности сферы.
        Args:
            radius(Union[int, float]): Принимает радиус сферы.
        Returns:
            Union[int, float]: Возвращает площадь поверхности сферы.
        """
        return 4 * 3.14 * radius ** 2
