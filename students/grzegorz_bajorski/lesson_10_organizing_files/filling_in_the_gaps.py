import os
import fnmatch
import shutil


prefix="spam*.txt"
files_list = []

for filename in os.listdir():
    if fnmatch.fnmatch(filename, prefix):
        files_list.append(filename)

files_list.sort()

prev_num = 0
for files in files_list:
    current_num = int(files.split("spam")[1].split(".")[0])
    expected_num = prev_num + 1
    if current_num != expected_num:
        new_name = "spam" + str(expected_num) + ".txt"
        expected_num = current_num
        shutil.move(files, new_name)
    prev_num += 1
print(files_list)
