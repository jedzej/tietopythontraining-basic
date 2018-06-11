import os
import re

text_files = []

for file in os.listdir('.'):
    if file.endswith(".txt"):
        text_files.append(file)

regex = re.compile(r'{}'.format(input("Enter regular expression: ")))

for file in text_files:
    current_file = open(file)
    file_content = current_file.readlines()
    for line in file_content:
        mo = regex.match(line)
        if mo is not None:
            print(line.strip())

    current_file.close()
