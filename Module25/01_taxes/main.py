from property import Car, Apartment, CountryHouse


def get_positive_float(user_input: str) -> float | None:
    """Преобразует ввод пользователя в положительное число.

    Args:
        user_input (str): Введённое пользователем значение.

    Returns:
        float | None: Число с плавающей точкой, если ввод корректный,
        иначе None.
    """
    try:
        value = float(user_input.replace(',', '.'))
        if value > 0:
            return value
        raise ValueError()
    except ValueError:
        print('Ошибка ввода: должно быть введено положительное число.')
        return None


def input_request(prompt: str) -> float:
    """Запрашивает у пользователя ввод до получения корректного значения.

    Args:
        prompt (str): Сообщение для ввода.

    Returns:
        float: Корректное число.
    """
    while True:
        value = get_positive_float(input(prompt))
        if value is not None:
            return value


def get_property_costs() -> tuple[float, float, float, float]:
    """Запрашивает у пользователя данные о финансах и стоимости имущества.

    Returns:
        tuple[float, float, float, float]: Количество денег,
        стоимость машины, квартиры и дачи.
    """
    money = input_request('Введите количество денег: ')
    car_cost = input_request('Введите стоимость машины: ')
    apartment_cost = input_request('Введите стоимость квартиры: ')
    country_house_cost = input_request('Введите стоимость дачи: ')
    return money, car_cost, apartment_cost, country_house_cost


def main() -> None:
    """Основная функция программы: рассчитывает налоги и проверяет,
    хватает ли у пользователя денег на их оплату.
    """
    money, car_cost, apartment_cost, country_house_cost = get_property_costs()

    car = Car(car_cost)
    car_tax = car.tax_calculation()
    print('\nНалог на машину: {:.2f} руб.'.format(car_tax))

    apartment = Apartment(apartment_cost)
    apartment_tax = apartment.tax_calculation()
    print('Налог на квартиру: {:.2f} руб.'.format(apartment_tax))

    country_house = CountryHouse(country_house_cost)
    country_house_tax = country_house.tax_calculation()
    print('Налог на дачу: {:.2f} руб.'.format(country_house_tax))

    common_tax = car_tax + apartment_tax + country_house_tax
    print('\nОбщая сумма: {:.2f} руб.'.format(common_tax))

    if money >= common_tax:
        print('Денег хватает для оплаты налогов.')
    else:
        difference = common_tax - money
        print('Для оплаты налогов не хватает {:.2f} руб.'.format(difference))


if __name__ == "__main__":
    main()
