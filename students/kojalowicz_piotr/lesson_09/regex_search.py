import os
import re


files = []

for file in os.listdir(os.getcwd()):
    if file.endswith(".txt"):
        files.append(file)

regex = re.compile(r'\d{2}-\d{3}')

for file in files:
    current_file = open(file)
    file_content = current_file.readlines()
    for line in file_content:
        mo = regex.search(line)
        if mo is not None:
            print(line.strip())
    current_file.close()
