import zipfile
import json


def open_zip_file():
    zip_file = zipfile.ZipFile('voina-i-mir.zip')
    zip_file.extractall()


def create_analysis_dict():
    text_file = open('voyna-i-mir.txt', encoding='utf-8')
    text = text_file.read()
    text_file.close()

    analysis = dict()

    symbols = sorted({symbol for symbol in text if symbol.isalpha()})
    for symbol in symbols:
        analysis[text.count(symbol)] = symbol

    return dict(sorted(analysis.items()))


print(json.dumps(create_analysis_dict(), ensure_ascii=False, indent=4))
