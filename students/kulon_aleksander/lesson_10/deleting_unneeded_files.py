import os

path = '/home/'
size_limit = 100048576


def main():
    for folder_name, sub_folder, file_names in os.walk(path):
        for file_name in file_names:
            file_path = os.path.join(folder_name, file_name)
            file_size = os.path.getsize(file_path)
            if os.path.isfile(file_path) and file_size > size_limit:
                print(file_path)


if __name__ == "__main__":
    main()
