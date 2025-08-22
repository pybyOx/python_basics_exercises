from _collections_abc import Iterable
import os


def count_string(directory: str) -> Iterable[tuple[str, int]]:
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as my_file:
                    count = 0
                    for line in my_file:
                        line = line.strip()
                        if line and not line.startswith('#'):
                            count += 1
                    yield file_path, count


strings = count_string(os.path.abspath(os.path.join('../..', 'Module26')))
for path, count in strings:
    print(f"{path}: {count} строк(и)")
