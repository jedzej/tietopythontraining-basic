import re
import os


print("Enter regex expression:")
regex = input(str())
search_exp = re.compile(regex)

for files in os.listdir('.'):
    if files.endswith(".txt"):
        opened_file = open(files, 'r')
        for line in opened_file:
            if search_exp.match(line):
                print("Found in " + files + "\n")
