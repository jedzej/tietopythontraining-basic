import re
import os
import argparse
import sys


def arg_input(args):
    parser = argparse.ArgumentParser(description="Filling in the gaps program")
    parser.add_argument('-d', '--source', help="Source directory",
                        default="/home/rybaapau/test")
    parser.add_argument('-p', '--prefix', help="Filename prefix",
                        default="spam")
    parser.add_argument('-s', '--suffix', help="Filename suffix",
                        required=True)
    results = parser.parse_args(args)
    return results.source, results.prefix, results.suffix


source, prefix, suffix = arg_input(sys.argv[1:])
pattern = re.compile(prefix + r'.*(\d{3})' + suffix)


def filling_the_gaps(folder):
    for foldername, subfolders, filenames in os.walk(folder):
        index = 0
        for filename in sorted(filenames):
            if pattern.match(filename):
                index += 1
                new_filename = prefix + str(index).zfill(3) + suffix

                print("Old: {}, new: {}".format(filename, new_filename))

                filename_path = os.path.join(foldername, filename)
                new_filename_path = os.path.join(foldername, new_filename)
                os.rename(filename_path, new_filename_path)


if __name__ == '__main__':
    filling_the_gaps(source)
    print('The end')
