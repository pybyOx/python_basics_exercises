def find_winners() -> list:
    with open('first_tour.txt', 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    passing_score = int(lines[0])  # минимальный проходной балл
    participants = lines[1:]  # остальные строки — участники

    winners = []
    for participant in participants:
        surname, name, score = participant.split()
        score = int(score)
        if score > passing_score:
            winners.append((score, surname, name[0]))  # сохраняем: баллы, фамилия, первая буква имени

    winners.sort(reverse=True, key=lambda x: x[0])  # сортируем по убыванию баллов
    return winners


def write_file_for_winners(winners: list):
    with open('second_tour.txt', 'w', encoding='utf-8') as f:
        f.write(str(len(winners)) + '\n')
        for i, (score, surname, initial) in enumerate(winners, start=1):
            f.write(f"{i}) {initial}. {surname} {score}\n")


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        print(f"\nСодержимое файла {file_name}:\n{f.read()}")


winners_list = find_winners()
write_file_for_winners(winners_list)
read_file('first_tour.txt')
read_file('second_tour.txt')
