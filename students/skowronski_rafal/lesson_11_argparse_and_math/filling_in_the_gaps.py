import re
from operator import itemgetter
import os
from os import listdir
from os.path import isfile
from os.path import join
import argparse


def list_files(search_directory):
    return [(file_name, search_directory) for file_name
            in listdir(search_directory)
            if isfile(join(search_directory, file_name))]


def get_decomposition(files, prefix):
    collection = []

    pattern = r'^{0}(?P<index>\d+)(?P<suffix>.*)$'.format(prefix)
    regex = re.compile(pattern)

    for file_name, file_dir in files:
        match = regex.match(file_name)

        if match is None:
            continue

        index = match.group('index')
        index_num = int(index)
        suffix = match.group('suffix')

        collection.append(
            (file_name, file_dir, prefix, index, suffix, index_num))

    return collection


def get_files_to_rename(files, file_prefix):
    collection = []
    files_decomposition = get_decomposition(files, file_prefix)
    files_decomposition.sort(key=itemgetter(5))

    next_index = None

    for file_name, file_dir, prefix, index, suffix, index_num \
            in files_decomposition:

        if next_index is None:
            next_index = index_num
            continue

        next_index = next_index + 1

        if index_num == next_index:
            continue

        index_length = len(index)
        new_index = str(next_index).zfill(index_length)
        new_name = prefix + new_index + suffix

        collection.append((file_name, new_name, file_dir))

    return collection


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Filling in the Gaps')
    parser.add_argument('search_directory',
                        help='directory to search for files')
    parser.add_argument('file_prefix',
                        help='files prefix to match')
    parser.add_argument('--quiet', '-q', action='store_true', default=False,
                        dest='quiet', help='suppress all normal output')

    args = parser.parse_args()

    search_directory = args.search_directory
    file_prefix = args.file_prefix
    quiet = args.quiet

    files = list_files(search_directory)

    files_to_rename = get_files_to_rename(files, file_prefix)

    for old_name, new_name, directory in files_to_rename:
        old_path = join(directory, old_name)
        new_path = join(directory, new_name)
        os.rename(old_path, new_path)

        if quiet:
            continue

        print()
        print('Renamed: ')
        print(' ' * 5 + 'Directory: {0}'.format(directory))
        print(' ' * 5 + 'Old name: {0}'.format(old_name))
        print(' ' * 5 + 'New name: {0}'.format(new_name))
