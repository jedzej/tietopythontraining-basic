import os


def search_large_files(folder_tree):
    for folders, subfolders, files in os.walk(folder_tree):
        for i in files:
            if os.path.getsize(os.path.join(folders, i)) > 100000000:
                print("Size: {} File: {}".format(os.path.getsize(
                    os.path.join(folders, i)), os.path.join(folders, i)))


location = 'C:\\Users\\wachumar\\Desktop\\książki'
search_large_files(location)
