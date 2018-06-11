import glob
import os
import shutil


def create_folder(name_folder):
    folder_path = name_folder + "/"
    if os.path.exists(folder_path):
        shutil.rmtree(folder_path)
    os.mkdir(folder_path)
    return folder_path


def search_for_jpg_and_txt(folder_path):
    for extension in (".pdf", ".txt"):
        for path in glob.glob("./**/*" + extension, recursive=True):
            shutil.copy2(path, folder_path)


def main():
    search_for_jpg_and_txt(create_folder("new_folder"))


if __name__ == "__main__":
    main()
