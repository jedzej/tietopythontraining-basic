#! python3
import os
import shutil
import argparse


def create_test_file(filename):
    with open(filename, "w") as f:
        f.write("foobar")


def create_test_tree(source_dir, destination_dir):
    if os.path.exists(source_dir):
        shutil.rmtree(source_dir)
    os.mkdir(source_dir)
    if os.path.exists(destination_dir):
        shutil.rmtree(destination_dir)
    os.mkdir(destination_dir)

    cats_dir = os.path.join(source_dir, "cats")
    waffles_dir = os.path.join(source_dir, "walnut", "waffels")
    os.makedirs(cats_dir)
    os.makedirs(waffles_dir)

    create_test_file(os.path.join(source_dir, "spam1.jpg"))
    create_test_file(os.path.join(source_dir, "spam2.jpg"))
    create_test_file(os.path.join(cats_dir, "catnames.txt"))
    create_test_file(os.path.join(cats_dir, "catphoto.jpg"))
    create_test_file(os.path.join(waffles_dir, "butter.pdf"))
    create_test_file(os.path.join(waffles_dir, "jam.jpg"))


def main():
    parser = argparse.ArgumentParser(description='Selective Copy program')

    parser.add_argument('-s',
                        help="Source directory.",
                        dest='src_dir',
                        required=True)
    parser.add_argument('-d',
                        help="Destination directory.",
                        dest='dest_dir',
                        required=True)
    parser.add_argument('--file-extension',
                        nargs='+', type=str,
                        required=True,
                        help='File extensions to be searched.')
    parser.add_argument('-c', action='store_true',
                        dest='create_tt',
                        help='Create test tree.')

    args = parser.parse_args()

    if args.create_tt:
        create_test_tree(args.src_dir, args.dest_dir)

    for foldername, _, filenames in os.walk(args.src_dir):
        for filename in filenames:
            if filename.endswith(tuple(args.file_extension)):
                filepath = os.path.join(foldername, filename)
                print(filepath)
                shutil.copy(filepath, args.dest_dir)


if __name__ == "__main__":
    main()
