import random
from monsters import MonsterBerserk, MonsterHunter
from heroes import Tank, Healer, Attacker


def one_year_of_war():  # Функция запускает симуляцию одного года сражений.

    # Вы можете изменять состав команды, НО размер команды не должен быть более 5.

    tank = Tank("Танк Пётр")
    attacker = Attacker("Убийца Ольга")
    second_attacker = Attacker("Убийца Траур")
    healer = Healer("Монах Игнат")
    second_healer = Healer("Монах Ирэна")
    good_team = [tank, attacker, second_attacker, second_healer, healer]

    # Код ниже изменять нельзя!

    if sum([isinstance(hero, (MonsterHunter, MonsterBerserk)) for hero in good_team]) > 1:
        print("В команде героев может быть только 1 монстр!")
        return 0

    evil_names = ["Абвыргл", "Мефисто", "Драник", "Диабло", "Пусечка", "Стаут"]
    mob_warrior = MonsterBerserk("Берсерк " + random.choice(evil_names))
    mob_ranger = MonsterHunter("Рейнджер " + random.choice(evil_names))
    evil_team = [mob_warrior, mob_ranger]

    for day in range(1, 366):  # запускается 365 итераций (1 итерация = 1 день)
        print("=" * 50 + "\nНачало дня №" + str(day) + "\n" + "=" * 50)

        # Каждый день каждый герой и монстр выбирают и совершают ОДНО действие.

        print("\nКоманда добра:\n" + '-' * 50)
        for hero in good_team:
            hero.make_a_move(good_team, evil_team)

        print("\nКоманда зла:\n" + '-' * 50)
        for mob in evil_team:
            mob.make_a_move(evil_team, good_team)

        print(f"Итоги дня сражений №{day}")

        # В итогах дня у каждого героя и каждого монстра вызывается метод __str__
        print("\nКоманда добра:\n" + '-' * 50)
        for hero in good_team:
            print(hero)

        print("\nКоманда зла:\n" + '-' * 50)
        for mob in evil_team:
            print(mob)

        # Мёртвые монстры удаляются из списка
        evil_team = [mob for mob in evil_team if mob.is_alive()]
        # Новые монстры в чётные дни добавляются в список (но их не может быть больше 4)
        if day % 2 == 0 and len(evil_team) < 4:
            newborn_evils = [MonsterBerserk("Берсерк " + random.choice(evil_names)),
                             MonsterHunter("Рейнджер " + random.choice(evil_names))]
            evil_team.append(random.choice(newborn_evils))

        # Если умирают герои - цикл завершается - битва считается проигранной (возвращается 0)
        if any([not hero.is_alive() for hero in good_team]):
            print("Вы проиграли!")
            return 0
        else:
            print("\nСражение продолжается!\n")

    # Если герои выживают - битва считается выигранной (возвращается 1)
    else:
        print("Вы одержали победу!")
        return 1


# Код ниже не подлежит изменению.
# Он запускает 20 симуляций. Для зачёта по заданию вам надо стабильно набирать 10 или более побед.
count_of_wins = 0
for year in range(1, 21):
    count_of_wins += one_year_of_war()

print("Из 20 раз команда героев одержала", count_of_wins, "побед")
if count_of_wins < 10:
    print("Героям нужна другая тактика, попробуйте ещё!")
else:
    print("Герои готовы к реальному сражению, задание выполнено!")
