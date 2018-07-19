import os
import shutil


def selective_copy(folder_path, new_folder_path):
    if not os.path.exists(new_folder_path):
        os.makedirs(new_folder_path)
    for folder_name, sub_folders, file_names in os.walk(folder_path):
        for file_name in file_names:
            if file_name.endswith('.pdf') or file_name.endswith('.jpg'):
                shutil.copy(os.path.join(folder_name, file_name),
                            new_folder_path)
                print("Copy {}".format(
                    os.path.normpath(os.path.join(folder_name, file_name))))


def main():
    folder_path = '../lesson_10/test'
    new_folder_path = 'new folder'
    selective_copy(folder_path, new_folder_path)


if __name__ == "__main__":
    main()
