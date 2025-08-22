class Property:
    def __init__(self, worth):
        self.__worth = worth

    def tax_calculation(self, fraction):
        return self.__worth * fraction


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self, fraction=1/1000):
        return super().tax_calculation(fraction)


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self, fraction=1/200):
        return super().tax_calculation(fraction)


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self, fraction=1/500):
        return super().tax_calculation(fraction)
