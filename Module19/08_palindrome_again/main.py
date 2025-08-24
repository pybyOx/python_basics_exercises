from collections import Counter


text = input("Введите строку: ")

counts = Counter(text)

odd_count = sum(1 for c in counts.values() if c % 2 != 0)

if odd_count > 1:
    print("Нельзя сделать палиндромом")
else:
    print("Можно сделать палиндромом")
