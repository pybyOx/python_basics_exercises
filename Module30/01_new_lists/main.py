from functools import reduce

floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers = [22, 33, 10, 6894, 11, 2, 1]

new_floats = list(map(lambda elem: round(elem ** 3, 3), floats))
print(new_floats)

new_names = list(filter(lambda elem: elem if len(elem) >= 5 else None, names))
print(new_names)

new_numbers = reduce((lambda a, b: a * b), numbers)
print(new_numbers)
