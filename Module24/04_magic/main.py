def print_result(elem_1, elem_2, reaction):
    print('{} + {} = {}'.format(elem_1, elem_2, reaction))


class Pyro:
    elem = 'Огонь'

    def __add__(self, other):
        if isinstance(other, Hydro):
            return Vaporize()
        elif isinstance(other, Electro):
            return Overloaded()
        elif isinstance(other, Cryo):
            return Melt()
        elif isinstance(other, Dendro):
            return Burning()
        elif isinstance(other, Anemo):
            return Swirl()
        else:
            return NoneReaction()


class Hydro:
    elem = 'Вода'

    def __add__(self, other):
        if isinstance(other, Pyro):
            return Vaporize()
        elif isinstance(other, Electro):
            return ElectroCharged()
        elif isinstance(other, Cryo):
            return Frozen()
        elif isinstance(other, Dendro):
            return Bloom()
        elif isinstance(other, Anemo):
            return Swirl()
        else:
            return NoneReaction()


class Electro:
    elem = 'Электричество'

    def __add__(self, other):
        if isinstance(other, Pyro):
            return Overloaded()
        elif isinstance(other, Hydro):
            return ElectroCharged()
        elif isinstance(other, Cryo):
            return Superconduct()
        elif isinstance(other, Dendro):
            return Catalyze()
        elif isinstance(other, Anemo):
            return Swirl()
        else:
            return NoneReaction()


class Cryo:
    elem = 'Мороз'

    def __add__(self, other):
        if isinstance(other, Pyro):
            return Melt()
        elif isinstance(other, Hydro):
            return Frozen()
        elif isinstance(other, Electro):
            return Superconduct()
        elif isinstance(other, Anemo):
            return Swirl()
        else:
            return NoneReaction()


class Dendro:
    elem = 'Растения'

    def __add__(self, other):
        if isinstance(other, Pyro):
            return Burning()
        elif isinstance(other, Hydro):
            return Bloom()
        elif isinstance(other, Electro):
            return Catalyze()
        else:
            return NoneReaction()


class Anemo:
    elem = 'Воздух'

    def __add__(self, other):
        if isinstance(other, (Pyro, Hydro, Electro, Cryo)):
            return Swirl()
        else:
            return NoneReaction()


class Geo:
    elem = 'Земля'

    def __add__(self, other):
        if isinstance(other, (Pyro, Hydro, Electro, Cryo)):
            return Crystallize()
        else:
            return NoneReaction()


class Vaporize:
    result = 'Пар'


class Overloaded:
    result = 'Перегрузка'


class Melt:
    result = 'Таяние'


class Burning:
    result = 'Горение'


class Swirl:
    result = 'Рассеивание'


class ElectroCharged:
    result = 'Заряжен'


class Frozen:
    result = 'Заморозка'


class Bloom:
    result = 'Бутонизация'


class Superconduct:
    result = 'Сверхпроводник'


class Catalyze:
    result = 'Катализ'


class Crystallize:
    result = 'Кристаллизация'


class NoneReaction:
    result = 'Реакция отсутствует'


element_1 = Hydro()
element_2 = Pyro()
result = element_1.__add__(element_2)
print_result(element_1.elem, element_2.elem, result.result)
