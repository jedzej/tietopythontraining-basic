import argparse
import os
import re
import sys


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='script to fill the gaps'
                                                 ' in filenames')

    parser.add_argument('-d', '--directory',
                        help='directory path',
                        required=True)

    parser.add_argument('-p', '--prefix',
                        help='file name prefix',
                        required=True)

    parser.add_argument('-e', '--extension',
                        help='file extension',
                        required=True)

    results = parser.parse_args(args)
    return (results.directory,
            results.prefix,
            results.extension)


def fill_the_gaps(directory_path, prefix_file_name, extension):
    start_number = 0
    for filename in sorted(os.listdir(directory_path)):

        if re.match(r"{0}\d{{3}}.{1}$".format
                    (prefix_file_name, extension), filename):
            number_expected = start_number + 1
            correct_file_name = (prefix_file_name +
                                 '0' *
                                 (3 - len(str(number_expected))) +
                                 str(number_expected) + '.txt')
            if correct_file_name != filename:
                rename_file(filename, number_expected, directory_path,
                            extension, prefix_file_name)

            start_number = number_expected


def rename_file(old_filename, index_file, directory, ext, pref_filename):
    old_path = os.path.join(directory, old_filename)
    new_name = "{}{:03d}.{}".format(pref_filename, index_file, ext)
    new_path = os.path.join(directory, new_name)
    os.rename(old_path, new_path)


def main():
    d, p, e = check_arg(sys.argv[1:])
    fill_the_gaps(d, p, e)


if __name__ == '__main__':
    main()
