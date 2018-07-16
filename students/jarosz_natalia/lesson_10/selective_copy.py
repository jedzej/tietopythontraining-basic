import os
import shutil


def selective_copy(folder_path, new_folder_path):
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith('.pdf') or filename.endswith('.jpg'):
                shutil.copy(os.path.join(foldername, filename),
                            new_folder_path)
                print("Copy {}".format(os.path.join(foldername, filename)))


def main():
    folder_path = '../lesson_10/test'
    new_folder_path = 'new folder'
    selective_copy(folder_path, new_folder_path)


if __name__ == "__main__":
    main()
