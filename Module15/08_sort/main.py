numbers = [1, 4, -3, 0, 10]
print('Изначальный список:', numbers)

for i in range(len(numbers)):
    mn = i
    for j in range(i + 1, len(numbers)):
        if numbers[j] < numbers[mn]:
            mn = j
    numbers[i], numbers[mn] = numbers[mn], numbers[i]

print('Отсортированный список:', numbers)
