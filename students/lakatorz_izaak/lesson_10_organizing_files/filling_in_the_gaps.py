# tested on bash commands:
#  touch test{01..030}.txt
# rm test0*5.txt
# rm test0*3.txt

import os
import re
import shutil

pattern = 'test0'
path = '../lesson_10_organizing_files/multifiles/'

prefix_pattern = re.compile('(?<={})\w+'.format(pattern))

numbers = []

for folderName, subfolder, filenames in os.walk(path):

    for filename in filenames:
        checker = re.search(prefix_pattern, filename)
        if checker is not None:
            numbers.append(int(checker.group(0)))

numbers = sorted(numbers)


for i in range(min(numbers), max(numbers)):

    if i < 10:
        test = path + pattern + '0' + str(i) + '.txt'
    else:
        test = path + pattern + str(i) + '.txt'

    if not os.path.isfile(test):
        j = i + 1
        while 1:
            if os.path.isfile(path + pattern + str(j) + '.txt'):
                break
            j = j + 1
        shutil.move(path + pattern + str(j) + '.txt', test)

