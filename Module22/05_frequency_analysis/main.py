from collections import Counter


def read_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        print(f"\nСодержимое файла {file_name}:\n{f.read()}")


alphabet = 'abcdefghijklmnopqrstuvwxyz'

with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read().lower()

letters = [char for char in text if char in alphabet]

winners = sorted(((char, cnt/len(letters)) for char, cnt in Counter(letters).items()),
                 key=lambda x: (-x[1], x[0]))  # сортировка: сначала по убыванию доли, потом по алфавиту

with open('analysis.txt', 'w', encoding='utf-8') as f:
    f.writelines(f"{char} {part:.3f}\n"
                 for char, part in winners)


read_file('text.txt')
read_file('analysis.txt')
