import os
import shutil
import re

PREFIX = "spam"
TEMP_FOLDER = "tmp"


def create_test_file(filename):
    with open(filename, "w") as test_file:
        test_file.write("Test...")


def create_test_files():
    if os.path.exists(TEMP_FOLDER):
        shutil.rmtree(TEMP_FOLDER)
    os.mkdir(TEMP_FOLDER)
    for i in range(1, 10):
        if i in [3, 7]:
            i += 1
        testfile_path = os.path.join(TEMP_FOLDER,
                                     "{}{:03d}".format(PREFIX, i))
        create_test_file(testfile_path)


def main():
    create_test_files()

    prev_num = 0
    for filename in os.listdir(TEMP_FOLDER):
        if re.match(r"{0}\d{{3}}".format(PREFIX), filename):
            curr_num = int(filename.split(PREFIX)[1])
            expected_num = prev_num + 1
            if curr_num != expected_num:
                old_path = os.path.join(TEMP_FOLDER, filename)
                new_path = os.path.join(TEMP_FOLDER, "{}{:03d}".format(
                                        PREFIX, expected_num))
                shutil.move(old_path, new_path)
                curr_num = expected_num
            prev_num = curr_num


if __name__ == "__main__":
    main()
