import os

MAX_SIZE = 100048576


def deleting(folder):
    for folder_name, sub_folders, file_names in os.walk(folder):
        for file_name in file_names:
            if (os.path.getsize(os.path.join(folder_name, file_name)) >
                    MAX_SIZE):
                print(os.path.join(folder_name, file_name))


def main():
    folder = '../lesson_10/test'
    deleting(folder)


if __name__ == "__main__":
    main()
