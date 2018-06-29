#! python 3
# selective_copy.py walks through a folder tree, searches for files with
# extension .jpg and copies them into a new folder.

import shutil
import os


def selective_copy(source, target):

    for file in os.listdir(source):
        if file.endswith('.jpg'):
            shutil.copy(os.sep.join([source, file]), target)


selective_copy('C:/Folder', 'C:/New_Folder')
print("Done")
