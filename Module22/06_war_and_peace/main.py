from zipfile import ZipFile
from collections import Counter


def extract_file():
    with ZipFile('voina-i-mir.zip', 'r') as zf:
        zf.extractall()


def create_analysis_dict():
    with open('voyna-i-mir.txt', 'r', encoding='utf-8') as f:
        text = f.read()

    return sorted(Counter([char for char in text if char.isalpha()]).items(),
                  key=lambda x: (-x[1], x[0]))  # сортируем: сначала по убыванию частоты, потом по символу


extract_file()
analysis = create_analysis_dict()

for symbol, count in analysis:
    print(f"{symbol}: {count}")
