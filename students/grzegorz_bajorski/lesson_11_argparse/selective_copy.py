import shutil
import os
import argparse


dest_dir = "copy_folder/"
os.mkdir(dest_dir)

parser = argparse.ArgumentParser(description='Selective Copy program')

parser.add_argument('-d',
                    help="Destination directory.",
                    dest='dest_dir',
                    required=True)

args = parser.parse_args()

dest_dir = args.dest_dir

for filename in os.listdir():
    if filename.endswith('.pdf'):
        print(filename)
        shutil.copy(filename, dest_dir)
    if filename.endswith('.txt'):
        print(filename)
        shutil.copy(filename, dest_dir)
