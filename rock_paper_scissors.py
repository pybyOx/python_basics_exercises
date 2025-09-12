rules = {
    "камень": "ножницы",
    "ножницы": "бумага",
    "бумага": "камень"
}

player_1 = input().strip()
player_2 = input().strip()

if player_1 == player_2:
    print("Ничья")
elif rules[player_1] == player_2:
    print("Выиграл игрок 1")
else:
    print("Выиграл игрок 2")
