def song_name_request(digit):
    name_song = input('Название {}-ой песни: '.format(digit + 1))
    return name_song


def create_user_list():
    count_of_songs = int(input('Сколько песен выбрать? '))
    user_list = [song_name_request(count) for count in range(count_of_songs)]
    return user_list


violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

user_songs = create_user_list()

print('Общее время звучания песен: {} минуты'.format(sum({violator_songs[song] for song in user_songs})))
