#! python3
import os
import shutil
import re

PREFIX_STRING = "spam"
TEST_DIR = "tmp"


def create_test_file(filename):
    with open(filename, "w") as f:
        f.write("foobar")


def create_test_files():
    if os.path.exists(TEST_DIR):
        shutil.rmtree(TEST_DIR)
    os.mkdir(TEST_DIR)
    for i in range(1, 10):
        # Introduce gaps
        if i in [2, 8]:
            i += 1
        testfile_path = os.path.join(TEST_DIR,
                                     "{}{:03d}".format(PREFIX_STRING, i))
        create_test_file(testfile_path)


def main():
    create_test_files()

    prev_num = 0
    for filename in os.listdir(TEST_DIR):
        if re.match(r"{0}\d{{3}}".format(PREFIX_STRING), filename):
            curr_num = int(filename.split(PREFIX_STRING)[1])
            expected_num = prev_num + 1
            if curr_num != expected_num:
                old_path = os.path.join(TEST_DIR, filename)
                new_path = os.path.join(TEST_DIR, "{}{:03d}".format(
                                        PREFIX_STRING, expected_num))
                shutil.move(old_path, new_path)
                curr_num = expected_num
            prev_num = curr_num


if __name__ == "__main__":
    main()
