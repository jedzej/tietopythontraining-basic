import os
import re
import sys
import shutil
import argparse


def main():
    d, pref = check_args(sys.argv[1:])
    files = [file for file in os.listdir(d) if file.startswith(pref)]
    files.sort()
    pattern = re.compile(r'\d{3}')

    if len(files) > 2:
        prev_n = None
        gap_found = False
        for file in files:
            curr_n = int(pattern.search(file).group())
            print("current {}".format(curr_n))
            if not gap_found:
                if prev_n is not None and prev_n + 1 != curr_n:
                    gap_found = True
            if gap_found:
                curr_n = prev_n + 1
                corr_file = re.sub(r'\d{3}', '{0:0>3}'.format(curr_n), file)
                old_path = os.path.join(d, file)
                new_path = os.path.join(d, corr_file)
                shutil.move(old_path, new_path)
            prev_n = curr_n


def check_args(args=None):
    parser = argparse.ArgumentParser(description='Big files detector')
    parser.add_argument('-d', '--directory',
                        help='Root directory path',
                        required=True)

    parser.add_argument('-p', '--prefix',
                        help='File prefix to look for',
                        required=True)

    result = parser.parse_args(args)
    return result.directory, result.prefix


if __name__ == '__main__':
    main()
