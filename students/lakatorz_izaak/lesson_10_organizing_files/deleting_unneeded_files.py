import os

path = '/home/'

for folderName, subfolder, filenames in os.walk(path):

    for filename in filenames:
        file_path = os.path.join(folderName, filename)
        file_size = os.path.getsize(file_path)
        if os.path.isfile(file_path) and file_size > 100048576:
            print(file_path)
