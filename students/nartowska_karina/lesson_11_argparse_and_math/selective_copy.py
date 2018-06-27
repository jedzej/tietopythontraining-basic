import shutil
import glob
import argparse
import sys


def check_arg(args=None):
    parser = argparse.ArgumentParser(description='Selective copy')
    parser.add_argument('-e', '--extension',
                        help='file extension',
                        required='True',
                        default='.txt')
    return parser.parse_args(args).extension


def main():
    ext = check_arg(sys.argv[1:])
    new_folder_path = "new/"

    for path in glob.glob('./**/*' + ext, recursive=True):
        shutil.copy2(path, new_folder_path)


if __name__ == "__main__":
    main()
