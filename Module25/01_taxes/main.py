from property import Car, Apartment, CountryHouse


def get_positive_float(user_input):
    try:
        value = float(user_input.replace(',', '.'))
        if value > 0:
            return value
        else:
            raise ValueError()
    except ValueError:
        print('Ошибка ввода: должно быть введено положительное число.')
        return None


def input_request(my_list, index):
    while True:
        value = get_positive_float(input(my_list[index]))
        if value is not None:
            break
    return value


def get_property_costs():
    list_input = ['Введите количество денег: ',
                  'Введите стоимость машины: ',
                  'Введите стоимость квартиры: ',
                  'Введите стоимость дачи: ']

    return [input_request(list_input, i) for i in range(4)]


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
