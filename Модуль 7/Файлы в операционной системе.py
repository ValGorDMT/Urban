import os
import time

os.chdir(r"D:\MyProgects\Urban\Модуль 7")
#print(os.getcwd())


directory = '.'
for root, dirs, files in os.walk(directory):
    print(f'>> root = "{root}", dirs = "{dirs}"')
    for i, file in enumerate(files):
        print(f'{i + 1}:', end=' ')
        filepath = os.path.join(root, file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(root)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
