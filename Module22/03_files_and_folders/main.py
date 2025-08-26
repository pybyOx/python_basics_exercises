import os


def count_files(path):
    dir_count, file_count, bytes_count = 0, 0, 0
    for struct in os.listdir(path):
        path_to_struct = os.path.join(path, struct)
        if os.path.isfile(path_to_struct):
            file_count += 1
            bytes_count += os.path.getsize(path_to_struct)
        else:
            dir_count += 1
            d, f, b = count_files(path_to_struct)
            dir_count += d
            file_count += f
            bytes_count += b

    return dir_count, file_count, bytes_count


directory = input('Путь до каталога: ')

dir_quantity, files_quantity, bytes_quantity = count_files(directory)

print('Размер каталога (в Кбайтах):', round(bytes_quantity / 1024, 2))
print('Количество подкаталогов:', dir_quantity)
print('Количество файлов:', files_quantity)
