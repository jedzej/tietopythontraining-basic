import os
import re

prefix = input('Prefix: ')
SUFFIX = '.txt'
PATH = 'C:\\Path\\to\\folder'

files_tab = []
regex = re.compile(r'^spam\d{3}\.txt$')

for _, _, files in os.walk(PATH):
    for file in files:
        mo = re.search(regex, file)
        if mo is not None:
            files_tab.append(file)

files_tab = sorted(files_tab)
number_of_files = len(files_tab)

new_names = []
for i in range(1, number_of_files + 1):
    new_names.append(prefix + "{:03d}".format(i) + SUFFIX)

for i in range(len(files_tab)):
    if new_names[i] != files_tab[i]:
        os.replace(PATH + '\\' + files_tab[i], PATH + '\\' + new_names[i])
