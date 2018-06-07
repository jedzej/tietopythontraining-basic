# tested on bash commands:
#  touch test{01..030}.txt
# rm test0*5.txt
# rm test0*3.txt

import os
import re
import shutil
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description='Gaps filling.')

    parser.add_argument(
        '--pattern', action="store",
        dest='pattern',
        required='True')

    parser.add_argument(
        '-p', action="store",
        dest='path',
        default='../lesson_11_argparse_and_math/multifiles/')

    results = parser.parse_args(sys.argv[1:])

    prefix_pattern = re.compile('(?<={})\w+'.format(results.pattern))

    numbers = []

    for folderName, subfolder, filenames in os.walk(results.path):

        for filename in filenames:
            checker = re.search(prefix_pattern, filename)
            if checker is not None:
                numbers.append(int(checker.group(0)))

    numbers = sorted(numbers)

    for i in range(min(numbers), max(numbers)):

        if i < 10:
            test = results.path + results.pattern + '0' + str(i) + '.txt'
        else:
            test = results.path + results.pattern + str(i) + '.txt'

        if not os.path.isfile(test):
            j = i + 1
            while 1:
                if os.path.isfile(results.path + results.pattern + str(j) +
                                  '.txt'):
                    break
                j = j + 1
            shutil.move(results.path + results.pattern + str(j) + '.txt', test)


if __name__ == '__main__':
    main()
