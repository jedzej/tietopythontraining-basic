import os
import glob


def main():
    max_file_size = 100 * 1024 * 1024
    current_path = os.path.expanduser(os.getcwd())
    for path in glob.glob(current_path + '**/*', recursive=True):
        size = os.path.getsize(path)
        if size >= max_file_size:
            print(path)


if __name__ == "__main__":
    main()
