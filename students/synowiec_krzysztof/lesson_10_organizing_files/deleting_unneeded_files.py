import os


ROOT_FOLDER = "original"
SIZE_LIMIT = 100000000


def main():
    big_files = []
    for root, folder, files in os.walk(ROOT_FOLDER):
        file_list = [os.path.join(root, file) for file in os.listdir(root)]
        for file in file_list:
            if not os.path.isdir(file):
                file_size = os.path.getsize(file)
                if file_size > SIZE_LIMIT:
                    big_files.append((file, file_size))

    for file, size in big_files:
        print("{} size: {} Bytes".format(file, size))


if __name__ == '__main__':
    main()
