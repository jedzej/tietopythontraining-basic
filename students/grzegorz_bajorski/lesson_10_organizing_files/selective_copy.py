import shutil
import os


dest_dir = "copy_folder/"
os.mkdir(dest_dir)

for filename in os.listdir():
    if filename.endswith('.pdf'):
        print(filename)
        shutil.copy(filename, dest_dir)
    if filename.endswith('.txt'):
        print(filename)
        shutil.copy(filename, dest_dir)
