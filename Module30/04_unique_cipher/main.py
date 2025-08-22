from typing import Optional
from collections import Counter


def count_unique_characters(text: str) -> Optional[int]:
    """Функция, считающая кол-во уникальных символов в строке."""
    letters_count = Counter(text.lower())
    return len(list(filter(lambda elem: letters_count[elem] == 1, letters_count)))


# Пример использования:
message = "Today is a beautiful day! The sun is shining and the birds are singing."

unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)
