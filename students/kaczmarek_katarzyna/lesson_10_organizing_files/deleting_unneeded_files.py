import os


def main():
    for folder_name, _, file_names in os.walk(input("Type a folder path: ")):
        for filename in file_names:
            file_path = os.path.join(folder_name, filename)
            # Instead of a size divisor of 1024 * 1024
            # I used the << bitwise shifting operator
            # 1<<20 to get megabytes, 1<<30 to get gigabytes, etc.
            file_size_mb = os.path.getsize(file_path) >> 20
            if file_size_mb > 100:
                print("{} {}MB".format(file_path, file_size_mb))


if __name__ == "__main__":
    main()
