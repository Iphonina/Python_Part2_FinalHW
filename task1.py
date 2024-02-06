# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её
# и все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер файлов
# в ней с учётом всех вложенных файлов и директорий.


import os
import json
import csv
import pickle


def save_directory_info(directory):
    data = []
    for root, dirs, files in os.walk(directory):
        total_size = 0
        for file in files:
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            total_size += size
            data.append({
                'path': path,
                'type': 'file',
                'size': size,
                'parent_directory': root
            })
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            dir_size = get_directory_size(dir_path)
            total_size += dir_size
            data.append({
                'path': dir_path,
                'type': 'directory',
                'size': dir_size,
                'parent_directory': root
            })
    save_as_json(data)
    save_as_csv(data)
    save_as_pickle(data)


def get_directory_size(directory):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def save_as_json(data):
    with open('directory_info.json', 'w') as f:
        json.dump(data, f)


def save_as_csv(data):
    with open('directory_info.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['path', 'type', 'size', 'parent_directory'])
        writer.writeheader()
        writer.writerows(data)


def save_as_pickle(data):
    with open('directory_info.pickle', 'wb') as f:
        pickle.dump(data, f)


# Пример использования
save_directory_info('/path/to/directory')
