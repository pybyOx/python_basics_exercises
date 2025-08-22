def find_winners():
    first_file = open('first_tour.txt', 'r')

    participants = [line.replace('\n', '') for line in first_file]

    passing_score = participants[0]
    participants.remove(participants[0])

    winners = dict()
    for participant in participants:
        info_participant = participant.split()
        if info_participant[2] > passing_score:
            winners[info_participant[2]] = info_participant[0], info_participant[1][:1]

    first_file.close()

    return dict(sorted(winners.items(), reverse=True))


def write_file_for_winners(dictionary):
    winners_file = open('second_tour.txt', 'w')
    winners_file.write(str(len(dictionary)))
    for count, point in enumerate(dictionary.keys()):
        winners_file.write('\n{}) {}.{} {}'.format(count + 1, dictionary[point][1], dictionary[point][0], point))
    winners_file.close()


def read_file(file_name):
    my_file = open(file_name, 'r')
    print('\nСодержимое файла {}:\n{}'.format(file_name, my_file.read()))
    my_file.close()


winners_dict = find_winners()
write_file_for_winners(winners_dict)
read_file('first_tour.txt')
read_file('second_tour.txt')
