import os

max_size = 100048576


def deleting(folder):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if (os.path.getsize(os.path.join(foldername, filename)) >
                    max_size):
                print(os.path.join(foldername, filename))


def main():
    folder = '../lesson_10/test'
    deleting(folder)


if __name__ == "__main__":
    main()
