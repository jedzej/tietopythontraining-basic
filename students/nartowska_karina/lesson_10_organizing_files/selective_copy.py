import shutil
import glob


def main():
    ext = input('Enter an extension, e.g .txt: ')
    new_folder_path = "new/"

    for path in glob.glob('./**/*' + ext, recursive=True):
        shutil.copy2(path, new_folder_path)


if __name__ == "__main__":
    main()
