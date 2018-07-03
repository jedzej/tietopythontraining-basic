import os
import glob


def main():
    humongous_file_size = 104857600
    tree = os.path.expanduser(
        '/home/user/Desktop/lesson_10_organizing_files/tree/')

    for path in glob.glob(tree + '**/*', recursive=True):
        size = os.path.getsize(path)
        if size >= humongous_file_size:
            print(path)


if __name__ == "__main__":
    main()
