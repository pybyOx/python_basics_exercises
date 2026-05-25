from monsters import MonsterBerserk, Monster


class Hero:
    """
    Базовый класс для всех героев.

    Attributes:
        max_hp (int | float): Максимальное  здоровье героя (по умолчанию 150).
        start_power (int | float): Базовая  сила героя (по умолчанию 10).
        name (str): Имя  героя.
        __hp (int | float): Текущее  здоровье.
        __power (int | float): Показатель  силы.
        __is_alive (bool): Флаг, жив ли герой.

    Methods:
        get_hp: Возвращает  текущее здоровье.
        set_hp: Устанавливает  новое здоровье (не меньше 0).
        get_power: Возвращает  силу.
        set_power: Устанавливает  силу.
        is_alive: Проверяет, жив ли герой.
        attack: Атаковать  цель (должен быть переопределён).
        take_damage: Получить урон.
        make_a_move: Сделать ход (усиление силы со временем).
        __str__: Строковое  представление героя (должно быть переопределено).
    """
    max_hp: int | float = 150
    start_power: int | float = 10

    def __init__(self, name: str) -> None:
        """
        Инициализирует героя.

        Args:
            name(str): Имя героя.
        """
        self.name: str = name
        self.__hp: int | float = self.max_hp
        self.__power: int | float = self.start_power
        self.__is_alive: bool = True

    def get_hp(self) -> int | float:
        """Возвращает текущее здоровье героя."""
        return self.__hp

    def set_hp(self, new_value: int | float) -> None:
        """
        Устанавливает новое значение hp.

        Если новое значение отрицательное, устанавливается hp = 0.
        Args:
            new_value(int | float): Новое значение hp
        """
        self.__hp = max(new_value, 0)

    def get_power(self) -> int | float:
        """Возвращает текущую силу героя."""
        return self.__power

    def set_power(self, new_power: int | float) -> None:
        """
        Устанавливает новое значение силы.

        Args:
            new_power(int | float): Новое значение силы.
        """
        self.__power = new_power

    def is_alive(self) -> bool:
        """Возвращает True, если герой жив, иначе False."""
        return self.__is_alive

    def attack(self, target: Monster) -> None:
        """
        Атака по переданной цели(target).

        Args:
            target(Monster): Враг, на которого направлена атака.
        Raises:
            NotImplementedError: Если метод не переопределен в дочерних классах.
        """
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage: int | float) -> None:
        """
        Получает урон и уменьшает hp.

        Если hp <= 0, герой умирает.

        Args:
            damage(int | float): Входящий урон.
        """
        print(f"\t{self.name} получил удар с силой равной = {round(damage)}. "
              f"Осталось здоровья - {round(self.get_hp())}.")
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends: list["Hero"], enemies: list[Monster]) -> None:
        """
        Базовый метод выбора действия героя.

        С каждым днём герои становятся всё сильнее(+0.1 к силе).

        Args:
            friends (list[Hero]): Список союзников
            enemies (list[Monster]): Список врагов
        """
        self.set_power(self.get_power() + 0.1)

    def __str__(self) -> str:
        """
        Описывает основные характеристики героя.

        Raises:
            NotImplementedError: Если метод не переопределен в дочерних классах.
        """
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):
    """
    Целитель — герой поддержки.

    Дополнительные атрибуты:
        __magic_power (int | float): магическая сила (равна 3 * power).

    Methods:
        attack: Наносит  половину урона
        take_damage: Получает  урон с множителем 1.2
        healing: Лечит  союзника на величину своей магической силы
        make_a_move: Если  союзник сильно ранен — лечит, иначе атакует
        __str__: Строковое  описание героя
    """
    def __init__(self, name: str) -> None:
        """
        Инициализирует Целителя.

        Args:
            name: Имя целителя.
        """
        super().__init__(name)
        self.__magic_power: int | float = self.get_power() * 3

    def __str__(self) -> str:
        """
        Описание основных характеристик целителя.
        Returns:
            str: HP, сила и магическая сила.
        """
        return (f"{self.name}"
                f" | HP : {round(self.get_hp())}"
                f" | Сила : {round(self.get_power())}"
                f" | Магия : {self.get_magic_power()}")

    def get_magic_power(self) -> int | float:
        """Возвращает магическую силу целителя."""
        return self.__magic_power

    def set_magic_power(self, new_value: int | float) -> None:
        """
        Устанавливает новое значение магической силы.

        Args:
            new_value (int | float): Новое значение магической силы.
        """
        self.__magic_power = new_value

    def attack(self, target: Monster) -> None:
        """
        Атака по переданной цели(target). Урон равен половине силы (power/2).
        Args:
            target(Monster): Враг, на которого направлена атака.
        """
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage: int | float) -> None:
        """
        Получает урон с множителем 1.2 (на 20% больше обычного).

        Args:
            damage(int | float): Входящий урон.
        """
        damage *= 1.2
        self.set_hp(self.get_hp() - damage)
        super().take_damage(damage)

    def healing(self, target: Hero) -> None:
        """
        Исцеляет союзника.

        Увеличивает здоровье цели на величину своей магической силы.

        Args:
            target (Hero): Союзник, которого лечат.
        """
        print(f"{self.name} исцеляет {target.name}")
        target.set_hp(target.get_hp() + self.get_magic_power())

    def make_a_move(self, friends: list[Hero], enemies: list[Monster]) -> None:
        """
        Выбирает действие: лечит или атакует.

        Если у союзника hp <= 90, лечит его.
        Иначе атакует ближайшего врага.

        Args:
            friends (list[Hero]): Список союзников.
            enemies (list[Monster]): Список врагов.
        """
        super().make_a_move(friends, enemies)
        print(self.name, end=' :')
        target_of_healing = min(friends, key=lambda f: f.get_hp())
        if target_of_healing.get_hp() <= 90:
            self.healing(target_of_healing)
        elif enemies:
            target = enemies[0]
            print(f"Атакую ближнего - {target.name}")
            self.attack(target)


class Tank(Hero):
    """
    Танк — герой-защитник.

    Дополнительные атрибуты:
        __defense (int | float): Показатель защиты (по умолчанию 1).
        __shield (bool): Флаг, поднят ли щит (по умолчанию False).

    Methods:
        attack: Наносит половину урона.
        take_damage: Делит входящий урон на показатель защиты.
        on_shield: Поднимает щит.
        off_shield: Опускает щит.
        make_a_move: Выбирает действие в зависимости от ситуации.
        __str__: Строковое описание героя.
    """
    def __init__(self, name: str) -> None:
        """
        Инициализирует Танка.
        Args:
            name: Имя Танка.
        """
        super().__init__(name)
        self.__defense: int | float = 1
        self.__shield: bool = False

    def __str__(self) -> str:
        """
        Описание характеристик танка.

        Returns:
            str: HP, сила, защита и состояние щита.
        """
        return (f"{self.name}"
                f" | HP : {round(self.get_hp())}"
                f" | Сила : {round(self.get_power())}"
                f" | Защита : {self.get_defense()}"
                f" | Щит : {self.get_shield()}")

    def get_defense(self) -> int | float:
        """Возвращает показатель защиты."""
        return self.__defense

    def set_defence(self, new_value: int | float) -> None:
        """
        Устанавливает новое значение защиты.

        Args:
            new_value (int | float): Новое значение защиты.
        """
        self.__defense = new_value

    def get_shield(self) -> bool:
        """Возвращает True, если щит поднят, иначе False."""
        return self.__shield

    def set_shield(self, new_value: bool) -> None:
        """
        Устанавливает новое значение флага поднятия щита.

        Args:
            new_value (bool): True — щит поднят, False — опущен.
        """
        self.__shield = new_value

    def attack(self, target: Monster) -> None:
        """
        Атака по переданной цели(target). Урон равен половине силы (power/2).
        Args:
            target(Monster): Враг, на которого направлена атака.
        """
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage: int | float) -> None:
        """
        Получает урон, деля его на показатель защиты.

        Args:
            damage(int | float): Входящий урон.
        """
        damage /= self.__defense
        self.set_hp(self.get_hp() - damage)
        super().take_damage(damage)

    def on_shield(self) -> None:
        """
        Поднимает щит.

        Увеличивает защиту в 2 раза и уменьшает силу в 2 раза.
        """
        if not self.get_shield():
            print(f"{self.name} поднимает щит.")
            self.set_shield(True)
            self.set_defence(self.get_defense() * 2)
            self.set_power(self.get_power() / 2)

    def off_shield(self) -> None:
        """
        Опускает щит.

        Уменьшает защиту в 2 раза и увеличивает силу в 2 раза.
        """
        if self.get_shield():
            print(f"{self.name} опускает щит.")
            self.set_shield(False)
            self.set_defence(self.get_defense() / 2)
            self.set_power(self.get_power() * 2)

    def make_a_move(self, friends: list[Hero], enemies: list[Monster]) -> None:  # - выбор действия - (атака, поднять щит/опустить щит)
        """
        Выбирает действие: поднять щит, опустить щит или атаковать.

        Если hp < 60 и щит не поднят — поднимает щит.
        Если hp > 100 и щит поднят — опускает щит.
        Иначе атакует врага (в первую очередь Берсерка).

        Args:
            friends (list[Hero]): Список союзников.
            enemies (list[Monster]): Список врагов.
        """
        super().make_a_move(friends, enemies)
        print(self.name, end=' :')
        if self.get_hp() < 60 and not self.get_shield():
            self.on_shield()
        elif self.get_hp() > 100 and self.get_shield():
            self.off_shield()
        elif enemies:
            berserk = next((e for e in enemies if isinstance(e, MonsterBerserk)), None)
            target = berserk if berserk else min(enemies, key=lambda e: e.get_hp())
            print(f"Атакую врага {target.name}")
            self.attack(target)


class Attacker(Hero):
    """
    Убийца — герой-нападающий.

    Дополнительные атрибуты:
        __power_multiply (int | float): Коэффициент усиления урона
            (входящего и исходящего), по умолчанию 2.

    Methods:
        attack: Наносит усиленный урон.
        take_damage: Получает усиленный входящий урон.
        power_up: Увеличивает коэффициент усиления.
        power_down: Уменьшает коэффициент усиления.
        make_a_move: Выбирает действие в зависимости от ситуации.
        __str__: Строковое описание героя.
    """
    def __init__(self, name: str) -> None:
        """
        Инициализирует Убийцу.
        Args:
            name: Имя Убийцы.
        """
        super().__init__(name)
        self.__power_multiply: int | float = 2

    def __str__(self) -> str:
        """
        Описание характеристик убийцы.
        Returns:
            str: HP, сила и коэффициент усиления.
        """
        return (f"{self.name}"
                f" | HP : {round(self.get_hp())}"
                f" | Сила : {round(self.get_power())}"
                f" | Усиление : {self.get_power_multiply()}")

    def get_power_multiply(self) -> int | float:
        """Возвращает коэффициент усиления урона."""
        return self.__power_multiply

    def set_power_multiply(self, new_value: int | float) -> None:
        """
        Устанавливает новое значение коэффициента усиления урона.

        Args:
            new_value (int | float): Новое значение коэффициента.
        """
        self.__power_multiply = new_value

    def attack(self, target: Monster) -> None:
        """
        Атака по переданной цели(target).

        Урон равен показателю силы, умноженному на коэффициент усиления урона(power * power_multiply).
        Args:
            target(Monster): Враг, на которого направлена атака.
        """
        target.take_damage(self.get_power() * self.get_power_multiply())

    def take_damage(self, damage: int | float) -> None:
        """
        Получает усиленный входящий урон.

        Урон умножается на половину коэффициента усиления.

        Args:
            damage (int | float): Входящий урон.
        """
        damage *= (self.get_power_multiply() / 2)
        self.set_hp(self.get_hp() - damage)
        super().take_damage(damage)

    def power_up(self) -> None:
        """Увеличивает коэффициент усиления урона в 2 раза."""
        self.set_power_multiply(self.get_power_multiply() * 2)
        print(f"{self.name} усиливается: множитель = {self.get_power_multiply()}")

    def power_down(self) -> None:
        """Уменьшает коэффициент усиления урона в 2 раза."""
        self.set_power_multiply(self.get_power_multiply() / 2)
        print(f"{self.name} ослабляется: множитель = {self.get_power_multiply()}")

    def make_a_move(self, friends: list[Hero], enemies: list[Monster]) -> None:  # - выбор действия - (атака, усиление, ослабление)
        """
        Выбирает действие: усиление, атака или ослабление.

        Если коэффициент < 2 — усиливается.
        Иначе атакует врага (в первую очередь Берсерка).

        Args:
            friends (list[Hero]): Список союзников.
            enemies (list[Monster]): Список врагов.
        """
        super().make_a_move(friends, enemies)
        print(self.name, end=' :')
        if self.get_power_multiply() < 2:
            self.power_up()
        elif enemies:
            berserk = next((e for e in enemies if isinstance(e, MonsterBerserk)), None)
            target = berserk if berserk else enemies[0]
            print(f"Атакую {target.name}")
            self.attack(target)
