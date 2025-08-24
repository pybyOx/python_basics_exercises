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

total_time = 0
for i in range(1, int(input('Сколько песен выбрать? ')) + 1):
    while True:
        song = input(f'Название {i}-ой песни: ')
        duration = violator_songs.get(song)
        if duration:
            total_time += duration
            break
        print('Такой песни нет в списке. Попробуй еще раз.')

print(f'\nОбщее время звучания песен: {round(total_time, 2)} минуты')
