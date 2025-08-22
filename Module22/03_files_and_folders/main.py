import os


def count_files(path, dir_count=0, file_count=0, bytes_count=0):
    for struct in os.listdir(path):
        path_to_struct = os.path.join(path, struct)
        if os.path.isfile(path_to_struct):
            file_count += 1
            bytes_count += os.path.getsize(path_to_struct)
        else:
            dir_count += 1
            dir_count, file_count, bytes_count = count_files(path_to_struct, dir_count, file_count, bytes_count)
    return dir_count, file_count, bytes_count


directory = input('Путь до каталога: ')

dir_quantity, files_quantity, bytes_quantity = count_files(directory)

print('Размер каталога (в Кбайтах):', bytes_quantity / 1024)
print('Количество подкаталогов:', dir_quantity)
print('Количество файлов:', files_quantity)
