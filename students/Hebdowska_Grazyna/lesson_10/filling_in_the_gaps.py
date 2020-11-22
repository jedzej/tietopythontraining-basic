import os
import re


searching_file = re.compile(r"""spam(\d\d\d).txt""")
from_folder = 'C:\\test1'

index = 0

for folderName, subfolders, filenames in os.walk(from_folder):
    for filename in sorted(filenames):
        if re.search(searching_file, filename):
            index += 1
            old_file = folderName + '\\' + filename
            new_file =\
                folderName + '\\' + 'spam' + str(index).zfill(3) + '.txt'
            os.rename(old_file, new_file)
