#! python3
import os
import shutil
import re
import argparse


def create_test_file(filename):
    with open(filename, "w") as f:
        f.write("foobar")


def create_test_files(test_dir, file_prefix):
    if os.path.exists(test_dir):
        shutil.rmtree(test_dir)
    os.mkdir(test_dir)
    for i in range(1, 10):
        # Introduce gaps
        if i in [2, 8]:
            i += 1
        testfile_path = os.path.join(test_dir,
                                     "{}{:03d}".format(file_prefix, i))
        create_test_file(testfile_path)


def main():
    parser = argparse.ArgumentParser(description='Filling In The Gaps program')
    parser.add_argument('-d', '--dir',
                        help="Directory path.",
                        dest='dir_path',
                        required=True)
    parser.add_argument('--file-prefix',
                        required=True,
                        help='File name prefix.')
    parser.add_argument('-c', action='store_true',
                        dest='create_tt',
                        help='Create test tree.')

    args = parser.parse_args()

    if args.create_tt:
        create_test_files(args.dir_path, args.file_prefix)

    prev_num = 0
    for filename in os.listdir(args.dir_path):
        if re.match(r"{0}\d{{3}}".format(args.file_prefix), filename):
            curr_num = int(filename.split(args.file_prefix)[1])
            expected_num = prev_num + 1
            if curr_num != expected_num:
                old_path = os.path.join(args.dir_path, filename)
                new_path = os.path.join(args.dir_path, "{}{:03d}".format(
                    args.file_prefix, expected_num))
                shutil.move(old_path, new_path)
                curr_num = expected_num
            prev_num = curr_num


if __name__ == "__main__":
    main()
