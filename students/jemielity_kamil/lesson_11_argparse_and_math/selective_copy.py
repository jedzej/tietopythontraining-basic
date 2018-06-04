import os
import shutil
import argparse


parser = argparse.ArgumentParser(description='Selective copy')
parser.add_argument('-e', action='store',
                    dest="extension", required=True,
                    help='extension')
args = parser.parse_args()

folder_path = 'C:\\Path\\to\\starting\\folder'
path_to_final_destination = 'C:\\Path\\to\\final\\destination'

extension = args.extension

for foldername, subfolders, filenames in os.walk(folder_path):
    for filename in filenames:
        if filename.endswith(extension):
            shutil.copy(os.path.join(foldername, filename), path_to_final_destination)