#!/usr/bin/env python3


import os
import sys
import re
import argparse
from operator import itemgetter


def check_arg(args=None):
    parser = argparse.ArgumentParser(description="Script for filling gaps "
                                     "for numbered files in given directory")
    parser.add_argument('-d', '--path',
                        help='path to directory',
                        required=True)
    parser.add_argument('-p', '--prefix',
                        help='prefix of numbered file, eg. image for image001',
                        required=True)

    results = parser.parse_args(args)

    return(results.path, results.prefix)


def main():
    count = 0

    dir_path, file_prefix = check_arg(sys.argv[1:])

    if not os.path.isdir(dir_path):
        print("There is not such directory")
        exit()

    split_match_files = []
    for file in os.listdir(dir_path):
        m = re.search(r"(^{})(\d+(?=.))(.+)".format(file_prefix), file)
        if m:
            split_match_files.append((m.group(1),
                                     int(m.group(2)),
                                     m.group(3),
                                     len(m.group(2))))

    if not len(split_match_files):
        print("There is not a single file that matches pattern for rename")
        exit()

    split_match_files.sort(key=itemgetter(1))
    first_number = split_match_files[0][1]

    for i, file in enumerate(split_match_files[1:]):
        proper_number = first_number + i + 1
        if file[1] != proper_number:
            file_name = "{}{}{}".format(file[0],
                                        str(file[1]).zfill(file[3]),
                                        file[2])
            new_file_name = "{}{}{}".format(file[0],
                                            str(proper_number).zfill(file[3]),
                                            file[2])
            os.rename(os.path.join(dir_path, file_name),
                      os.path.join(dir_path, new_file_name))
            print("Renamed {} to {}".format(file_name, new_file_name))
            count += 1

    if count:
        print("Renamed {} files in {}".format(count, dir_path))
    else:
        print("In {} there are no files which needs to be renamed"
              .format(dir_path))


if __name__ == "__main__":
    main()
