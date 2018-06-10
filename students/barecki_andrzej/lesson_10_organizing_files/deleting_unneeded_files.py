import os


def show_big_files(path, param_file_size):
    for folder_name, _, file_names in os.walk(path):
        for file_name in file_names:
            file_name_path = os.path.join(folder_name, file_name)
            current_file_size = os.path.getsize(file_name_path)
            if current_file_size > param_file_size:
                print("File: {0} has {1} bytes".format(file_name_path,
                                                       current_file_size))


def main():
    show_big_files(os.getcwd(), 1 << 26)


if __name__ == '__main__':
    main()
