old_card = [3070, 2060, 3090, 3070, 3090]

print('Количество видеокарт:', len(old_card))

for i in range(len(old_card)):
    print(i + 1, 'Видеокарта:', old_card[i])

max_card = max(old_card)

new_card = [card for card in old_card if card != max_card]

print('Старый список видеокарт:', old_card)
print('Новый список видеокарт:', new_card)

