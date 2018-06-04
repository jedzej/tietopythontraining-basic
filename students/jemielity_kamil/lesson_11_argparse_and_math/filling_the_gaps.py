import os
import re
import argparse

parser = argparse.ArgumentParser(description='Filling the gaps')
parser.add_argument('-p', action='store',
                    dest="prefix", required=True,
                    help='prefix')
args = parser.parse_args()


prefix = args.prefix
suffix = '.txt'
path = 'C:\\path\\to\\folder'

files_tab = []
regex = re.compile(r'^spam\d{3}\.txt$')

for folder, subfolders, files in os.walk(path):
    for file in files:
        mo = re.search(regex, file)
        if mo is not None:
            files_tab.append(file)

files_tab = sorted(files_tab)
number_of_files = len(files_tab)

new_names = []
for i in range(1, number_of_files+1):
    if i < 10:
        new_names.append(prefix + '00' + str(i) + suffix)
    elif 10 < i < 100:
        new_names.append(prefix + '0' + str(i) + suffix)
    else:
        new_names.append(prefix + str(i) + suffix)

for i in range(len(files_tab)):
    if new_names[i] != files_tab:
        os.replace(files_tab[i], new_names[i])