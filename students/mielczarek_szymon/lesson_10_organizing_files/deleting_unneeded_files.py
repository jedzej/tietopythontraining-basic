#! python3
import os


def main():
    for foldername, _, filenames in os.walk("D:"):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            filesize_mb = os.path.getsize(filepath) >> 20
            if filesize_mb > 100:
                print("{} {}MB".format(filepath, filesize_mb))


if __name__ == "__main__":
    main()
