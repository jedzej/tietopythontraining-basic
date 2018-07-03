import os
import shutil

path = '../lesson_10_organizing_files/'

new_dir = 'new_dir'

if not os.path.exists(new_dir):
    os.makedirs(new_dir)

for folder, subfolders, files in os.walk(path):
    for file in files:
        if file.endswith('.txt'):
            shutil.copy(file, '../' + new_dir)
