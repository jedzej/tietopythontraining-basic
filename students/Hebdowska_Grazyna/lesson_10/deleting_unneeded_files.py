import os


from_folder = input("Give the folder name where the unneeded files are: ")

for folderName, subfolders, filenames in os.walk(from_folder):
    for filename in filenames:
        source = folderName + '\\' + filename
        if os.path.getsize(source) > 100000000:
            print(source)
