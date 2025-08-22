from os import walk, path
from _collections_abc import Iterable


def gen_files_path(target_folder: str, directory='/') -> Iterable[str]:
    for root, dirs, files in walk(directory):
        if path.basename(root) == target_folder:
            return
        for file in files:
            yield path.join(root, file)


files_path = gen_files_path(target_folder='06_Abstract_class',
                            directory=path.abspath(path.join('../..', 'Module25')))
for file_path in files_path:
    print(file_path)
