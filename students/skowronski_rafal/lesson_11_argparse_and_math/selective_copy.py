import os
import re
from os import path
import shutil
import argparse


_names_history = {}


def get_target_file_name(source_file_name):
    if source_file_name not in _names_history:
        _names_history[source_file_name] = 0
        return source_file_name

    name_count = _names_history[source_file_name] + 1
    _names_history[source_file_name] = name_count

    name, extension = os.path.splitext(source_file_name)
    return name + '_{0}'.format(name_count) + extension


def ensure_empty_target_dir(target_dir):
    if os.path.exists(target_dir):
        if os.path.isfile(target_dir):
            os.remove(target_dir)
        else:
            shutil.rmtree(target_dir)

    os.mkdir(target_dir)


def copy_files(source_dir, target_dir, file_match, quiet):
    ensure_empty_target_dir(target_dir)

    regex = re.compile(file_match)

    for current_dir, sub_dirs, file_names in os.walk(source_dir):
        if current_dir == target_dir:
            continue

        files_to_copy = [
            (path.join(current_dir, file_name), file_name)
            for file_name in file_names if regex.match(file_name)]

        for file_path, file_name in files_to_copy:
            target_file_path = path.join(
                target_dir,
                get_target_file_name(file_name))

            shutil.copy(file_path, target_file_path)

            if not quiet:
                print('File copied:')
                print(' ' * 5 + 'Source: {0}'.format(file_path))
                print(' ' * 5 + 'Target: {0}'.format(target_file_path))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Selective Copy')

    parser.add_argument('source_directory',
                        help='source directory')
    parser.add_argument('target_directory',
                        help='target directory')
    parser.add_argument('file_match',
                        help='regular expression to match file name')
    parser.add_argument('--quiet', '-q', action='store_true', default=False,
                        dest='quiet', help='suppress all normal output')

    args = parser.parse_args()

    file_match = args.file_match
    source_dir = args.source_directory
    target_dir = args.target_directory
    quiet = args.quiet

    if not quiet:
        print('\nACHTUNG!!!')
        print('This program will copy all \'{0}\' files from {1} to {2}.'
              .format(file_match, source_dir, target_dir))
        yes_no = input('Do you want to continue? (y/n): ')
        if yes_no is not 'y':
            exit(0)

    copy_files(source_dir, target_dir, file_match, quiet)
