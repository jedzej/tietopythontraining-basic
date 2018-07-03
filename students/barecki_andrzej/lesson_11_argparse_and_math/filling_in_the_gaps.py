import os
import datetime
import re
import argparse
import sys


def create_example_test_files(path, source_folder_param):
    os.chdir(path)
    print('Current working directory:', os.getcwd() + os.linesep)
    src_dir = ""

    """Create source folder(extend date/time approach)"""
    if source_folder_param is not None:
        if os.path.exists(source_folder_param):
            random_folder = os.path.join(source_folder_param + '_' +
                                         str(datetime.datetime.now().date()) +
                                         '_' + str(datetime.datetime.now().
                                                   time()).replace(':', '.'))
            src_dir = random_folder
        else:
            src_dir = source_folder_param

    """ Create example of few files """
    file_list = [os.path.join(src_dir, "spam002.txt"),
                 os.path.join(src_dir, "spam003.tyt"),
                 os.path.join(src_dir, "spam004.txt"),
                 os.path.join(src_dir, "spam005.jpg"),
                 os.path.join(src_dir, "saam006.txt"),
                 os.path.join(src_dir, "saam007.mp3"),
                 os.path.join(src_dir, "spam007.txt"),
                 os.path.join(src_dir, "spam009.txt"),
                 ]

    for elem in file_list:
        if not os.path.exists(os.path.dirname(elem)):
            os.makedirs(os.path.dirname(elem))
        with open(elem, "w") as test_file:
            test_file.close()

    return os.path.join(os.getcwd(), src_dir)


def filling_in_the_gap(path, prefix, extension):
    spam_regex = re.compile(r'({0})(\d\d\d)({1})'.format(prefix, extension))
    init = False
    index = 0

    """search all files from a given directory"""
    for folder_name, _, file_names in os.walk(path):
        for filename in sorted(file_names):
            result = spam_regex.search(filename)
            if result is not None:
                """index initialization """
                if init is False:
                    index = int(result.group(2))
                    init = True
                    print("Initial file:{0}".format(os.path.join(folder_name,
                                                                 filename)))
                    print("Initial index:{0}".format(index) + os.linesep)
                else:
                    """ Update index """
                    index = index + 1
                    old_path = os.path.join(folder_name, filename)

                    """Generate filename"""
                    new_filename = "spam" + str(index).zfill(3) + ".txt"
                    new_path = os.path.join(folder_name, new_filename)
                    print("Before:{0}".format(old_path))

                    """Update filename"""
                    os.rename(old_path, new_path)
                    print("After: {0}".format(new_path))


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='filling_in_the_gap helper'
                                                 ' for validate parameters')
    parser.add_argument('-s', '--src_folder',
                        help='source folder',
                        default='source_filling_in_the_gaps')
    parser.add_argument('-p', '--prefix',
                        help='prefix in filename',
                        default='spam')
    parser.add_argument('-e', '--extension',
                        help='extension files',
                        default=".txt")

    results = parser.parse_args(args)
    return results.src_folder, results.prefix, results.extension


def main():
    src_folder_param, prefix_param, extension_param = check_arg(sys.argv[1:])

    source_path = create_example_test_files(os.getcwd(), src_folder_param)
    filling_in_the_gap(source_path, prefix_param, extension_param)
    print(os.linesep + "End program.")


if __name__ == '__main__':
    main()
