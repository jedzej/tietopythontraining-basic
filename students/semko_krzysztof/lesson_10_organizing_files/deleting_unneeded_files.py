"""
It’s not uncommon for a few unneeded but humongous files or
folders to take up the bulk of the space on your hard
drive. If you’re trying to free up room on your computer,
you’ll get the most bang for your buck by deleting
the most massive of the unwanted files.
But first you have to find them.

Write a program that walks through a folder tree and
searches for exceptionally large files or folders—say,
ones that have a file size of more than 100MB. (Remember,
to get a file’s size, you can use os.path.getsize() from
the os module.) Print these files with their
absolute path to the screen.
"""

import os
import send2trash


def find_and_delete(directory):
    for folderName, subfolders, filenames in os.walk(directory):
        for file in filenames:
            size = os.path.getsize(os.path.join(folderName, file))
            if size > 100:
                print(os.path.join(folderName, file), end=" size: ")
                print(os.path.getsize(os.path.join(folderName, file)), end=" bytes")
                print()

                # Files could be removed with commands below:
                # path = os.path.join(folderName, file)
                # os.unlink(path)
                # or with:
                # send2trash.send2trash(path)


def main():
    find_and_delete(os.path.join(os.getcwd(), "delete_unneeded"))


if __name__ == '__main__':
    main()
