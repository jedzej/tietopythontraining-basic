import os


def delete_unneeded(given_folder):

    for folders, subfolders, files in os.walk(given_folder):
        for file in files:
            if os.path.getsize(os.path.join(given_folder, file)) > 100000000:
                print(os.path.join(given_folder, file) + ' DELETING FILE')


delete_unneeded('C:\\Pajton')
