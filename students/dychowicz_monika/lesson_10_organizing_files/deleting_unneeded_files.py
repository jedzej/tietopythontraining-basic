import os

max_size = 100000000


def delete_unneeded_files(folder):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            filename = os.path.join(folder, filename)
            if os.path.getsize(filename) > max_size:
                print(filename)


if __name__ == '__main__':
    delete_unneeded_files(r"C:\Users\dychomon\Downloads")