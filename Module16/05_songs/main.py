violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

print('Сколько песен выбрать?', end=' ')
songs_amt = int(input())

total_time = 0

for count in range(songs_amt):

    print('Название', count + 1, '-й песни:', end=' ')
    name_song = input()

    for index in range(len(violator_songs)):
        if name_song == violator_songs[index][0]:
            total_time += violator_songs[index][1]

print('\nОбщее время звучания песен:', round(total_time, 2), 'минуты')
