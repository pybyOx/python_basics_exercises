containers = []

count = int(input('Количество контейнеров: '))
max_weight = 200
for _ in range(count):
    correct = False

    while not correct:
        weight = int(input('Введите вес контейнера: '))
        if weight <= 200 and weight <= max_weight:
            correct = True
            max_weight = weight
            containers.append(weight)
        else:
            print('Вес не должен превышать веса предыдущего контейнера и не должен быть больше 200.')


new_container = int(input('\nВведите вес нового контейнера: '))
for i in range(len(containers)):
    if containers[i] < new_container:
        print('\nНомер, который получит новый контейнер:', i + 1)
        break
