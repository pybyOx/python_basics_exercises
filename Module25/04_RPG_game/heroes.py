class Hero:

    max_hp = 150
    start_power = 10

    def __init__(self, name):
        self.name = name                        # - Имя
        self.__hp = self.max_hp                 # - Здоровье
        self.__power = self.start_power         # - Сила
        self.__is_alive = True                  # - Жив ли объект

    def get_hp(self):
        return self.__hp

    def set_hp(self, new_value):
        self.__hp = max(new_value, 0)

    def get_power(self):
        return self.__power

    def set_power(self, new_power):
        self.__power = new_power

    def is_alive(self):
        return self.__is_alive

    def attack(self, target):  # - Атаковать
        raise NotImplementedError("Вы забыли переопределить метод Attack!")

    def take_damage(self, damage):  # - Получить урон
        print("\t{} получил удар с силой равной = {}. Осталось здоровья - {}.".format(
            self.name, round(damage), round(self.get_hp())))
        if self.get_hp() <= 0:
            self.__is_alive = False

    def make_a_move(self, friends, enemies):  # make_a_move базового класса могут вызывать только герои, не монстры.
        self.set_power(self.get_power() + 0.1)  # С каждым днём герои становятся всё сильнее.

    def __str__(self):  # - Описать своё состояние
        raise NotImplementedError("Вы забыли переопределить метод __str__!")


class Healer(Hero):  # Целитель:
    def __init__(self, name):
        super().__init__(name)
        self.__magic_power = self.get_power() * 3      # - магическая сила

    def __str__(self):
        return ('{name} | HP : {hp} | Сила : {power}'
                ' | Магия : {magic}').format(name=self.name, hp=round(self.get_hp()), power=round(self.get_power()),
                                             magic=self.get_magic_power())

    def get_magic_power(self):
        return self.__magic_power

    def set_magic_power(self, new_value):
        self.__magic_power = new_value

    def attack(self, target):  # - атака - может атаковать врага, но атакует только в половину силы self.__power
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        damage *= 1.2  # получает на 20% больше урона (1.2 * damage)
        self.set_hp(self.get_hp() - damage)
        super().take_damage(damage)

    def healing(self, target):  # - исцеление - увеличивает здоровье цели на величину равную своей магической силе
        print("Исцеляю", target.name)
        target.set_hp(target.get_hp() + self.get_magic_power())

    def make_a_move(self, friends, enemies):  # - выбор действия - (атака, исцеление)
        super().make_a_move(friends, enemies)
        print(self.name, end=' :')
        target_of_healing = friends[0]
        min_health = target_of_healing.get_hp()
        for friend in friends:
            if friend.get_hp() < min_health:
                target_of_healing = friend
                min_health = target_of_healing.get_hp()
        if min_health <= 120:
            self.healing(target_of_healing)
        else:
            if not enemies:
                return
            print("Атакую ближнего -", enemies[0].name)
            self.attack(enemies[0])


class Tank(Hero):  # Танк:
    def __init__(self, name):
        super().__init__(name)
        self.__defense = 1              # - показатель защиты
        self.__shield = False          # - поднят ли щит

    def __str__(self):
        return ('{name} | HP : {hp} | Сила : {power}'
                ' | Защита : {defense} | Щит : {shield}').format(name=self.name, hp=round(self.get_hp()),
                                                                 power=round(self.get_power()),
                                                                 defense=self.get_defense(), shield=self.get_shield())

    def get_defense(self):
        return self.__defense

    def set_defence(self, new_value):
        self.__defense = new_value

    def get_shield(self):
        return self.__shield

    def set_shield(self, new_value):
        self.__shield = new_value

    def attack(self, target):  # - атака - наносит половину урона (self.__power)
        target.take_damage(self.get_power() / 2)

    def take_damage(self, damage):
        damage = damage / self.__defense  # - входящий урон делится на показатель защиты
        self.set_hp(self.get_hp() - damage)
        super().take_damage(damage)

    def on_shield(self):  # - поднять щит - увеличивает защиту в 2 раза, но уменьшает показатель силы в 2 раза.
        print('Поднимаю щит.')
        if self.get_shield() is False:
            self.set_shield(True)
            self.set_defence(self.get_defense() * 2)
            self.set_power(self.get_power() / 2)

    def off_shield(self):  # - опустить щит - уменьшает защиту в 2 раза, но увеличивает показатель силы в 2 раза.
        print('Опускаю щит.')
        if self.get_shield() is True:
            self.set_shield(False)
            self.set_defence(self.get_defense() / 2)
            self.set_power(self.get_power() * 2)

    def make_a_move(self, friends, enemies):  # - выбор действия - (атака, поднять щит/опустить щит)
        super().make_a_move(friends, enemies)
        print(self.name, end=' :')
        if self.get_hp() < 60 and self.get_shield() is False:
            self.on_shield()
        elif self.get_hp() > 100 and self.get_shield() is True:
            self.off_shield()
        else:
            if not enemies:
                return
            target_of_attack = enemies[0]
            min_health = target_of_attack.get_hp()
            for enemy in enemies:
                if enemy.get_hp() < min_health:
                    target_of_attack = enemy
                    min_health = target_of_attack.get_hp()
            print("Атакую врага с наименьшим HP -", target_of_attack.name)
            self.attack(target_of_attack)


class Attacker(Hero):  # Убийца:
    def __init__(self, name):
        super().__init__(name)
        self.__power_multiply = 2         # - коэффициент усиления урона (входящего и исходящего)

    def __str__(self):
        return ('{name} | HP : {hp} | Сила : {power}'
                ' | Усиление урона : {multiply}').format(name=self.name, hp=round(self.get_hp()),
                                                         power=round(self.get_power()),
                                                         multiply=self.get_power_multiply())

    def get_power_multiply(self):
        return self.__power_multiply

    def set_power_multiply(self, new_value):
        self.__power_multiply = new_value

    def attack(self, target):  # атака - наносит урон равный показателю силы, умноженному на коэффициент усиления урона
        target.take_damage(self.get_power() * self.get_power_multiply())
        self.power_down()

    def take_damage(self, damage):  # - получение урона - damage * (self.power_multiply / 2)
        damage = damage * (self.get_power_multiply() / 2)
        self.set_hp(self.get_hp() - damage)
        super().take_damage(damage)

    def power_up(self):  # - усиление (power_up) - увеличивает коэффициента усиления урона в 2 раза
        self.set_power_multiply(self.get_power_multiply() * 2)
        print('Усиление: усиление урона = ', self.get_power_multiply())

    def power_down(self):  # - ослабление (power_down) - уменьшает коэффициента усиления урона в 2 раза
        self.set_power_multiply(self.get_power_multiply() / 2)
        print('Ослабление: усиление урона = ', self.get_power_multiply())

    def make_a_move(self, friends, enemies):  # - выбор действия - (атака, усиление, ослабление)
        super().make_a_move(friends, enemies)
        print(self.name, end=' :')
        if self.get_power_multiply() < 2:
            self.power_up()
        else:
            if not enemies:
                return
            print("Атакую того, кто стоит ближе -", enemies[0].name)
            self.attack(enemies[0])
