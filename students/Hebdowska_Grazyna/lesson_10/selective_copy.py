import shutil
import os
import re


# Typy of searching file
searching_file_type = re.compile(r"""^(.*?).txt""")
# Here will be copied the file
destination = 'C:\\test1'
# source folder
from_folder = 'C:\\test'

for folderName, subfolders, filenames in os.walk(from_folder):
    for filename in filenames:
        if re.search(searching_file_type, filename):
            source = folderName + '\\' + filename
            shutil.copy(source, destination)
