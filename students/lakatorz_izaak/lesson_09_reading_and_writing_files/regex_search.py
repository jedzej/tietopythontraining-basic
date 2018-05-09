import os
import re


user_regex = re.compile(r'\d')

path = '../lesson_09_reading_and_writing_files/'

folder_files = os.listdir(path)

txt_files = [x for x in folder_files if x.endswith(".txt")]

for filename in txt_files:
    file = open(path + filename)
    for line in file.readlines():
        checked_line = user_regex.search(line)
        if checked_line is not None:
            print(filename + ' : ' + line)
