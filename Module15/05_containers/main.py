containers = [int(input('Введите вес контейнера: ')) for _ in range(int(input('Количество контейнеров: ')))]

new_container = int(input('Введите вес нового контейнера: '))
for i in range(len(containers)):
    if containers[i] < new_container:
        print('Номер, который получит новый контейнер:', i + 1)
        break
