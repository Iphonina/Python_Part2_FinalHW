# Соберите из созданных на уроке и в рамках домашнего задания функций пакет
# для работы с файлами.


# Для создания пакета для работы с файлами нужно создать директорию с именем пакета:
# file_utils/
#     __init__.py
#     file_operations.py

# В файле file_operations.py разместить функции для работы с файлами, например:
import os


def group_rename_files(desired_name, num_digits, original_extension, new_extension, start_range, end_range):
    file_list = [f for f in os.listdir('.') if f.endswith(original_extension)]
    counter = 1
    for filename in file_list:
        original_name = filename[start_range-1:end_range]
        new_name = original_name + desired_name + str(counter).zfill(num_digits) + new_extension
        os.rename(filename, new_name)
        counter += 1

# Затем в файле __init__.py можно импортировать функции из file_operations.py,
# чтобы они были доступны при импортировании пакета:

from .file_operations import group_rename_files

# Теперь можно установить пакет с помощью pip, чтобы он был доступен из любого места на системе:
# Выполнить команду для установки пакета:
pip install

# После установки пакета он готов к использованию, можно импортировать функции из него.
from file_utils import group_rename_files

group_rename_files("_new", 3, ".txt", ".doc", 3, 6)



