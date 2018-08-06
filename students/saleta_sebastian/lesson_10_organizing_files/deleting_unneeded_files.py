import os


def list_file_size(path):
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            file_size_in_mb = os.path.getsize(file_path) >> 20
            if file_size_in_mb > 100:
                print(file_path)
                print('{} size: {}'.format(file, os.path.getsize(file_path)))


def main():
    list_file_size(os.getcwd())


if __name__ == '__main__':
    main()
