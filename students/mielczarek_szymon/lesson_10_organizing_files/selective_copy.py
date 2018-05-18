#! python3
import os
import shutil

SOURCE_DIR = "tmp_src"
DESTINATION_DIR = "tmp_dest"


def create_test_file(filename):
    with open(filename, "w") as f:
        f.write("foobar")


def create_test_tree():
    if os.path.exists(SOURCE_DIR):
        shutil.rmtree(SOURCE_DIR)
    os.mkdir(SOURCE_DIR)
    if os.path.exists(DESTINATION_DIR):
        shutil.rmtree(DESTINATION_DIR)
    os.mkdir(DESTINATION_DIR)

    cats_dir = os.path.join(SOURCE_DIR, "cats")
    waffles_dir = os.path.join(SOURCE_DIR, "walnut", "waffels")
    os.makedirs(cats_dir)
    os.makedirs(waffles_dir)

    create_test_file(os.path.join(SOURCE_DIR, "spam1.jpg"))
    create_test_file(os.path.join(SOURCE_DIR, "spam2.jpg"))
    create_test_file(os.path.join(cats_dir, "catnames.txt"))
    create_test_file(os.path.join(cats_dir, "catphoto.jpg"))
    create_test_file(os.path.join(waffles_dir, "butter.pdf"))
    create_test_file(os.path.join(waffles_dir, "jam.jpg"))


def main():
    create_test_tree()

    for foldername, _, filenames in os.walk(SOURCE_DIR):
        for filename in filenames:
            if filename.endswith((".jpg", ".pdf")):
                filepath = os.path.join(foldername, filename)
                print(filepath)
                shutil.copy(filepath, DESTINATION_DIR)


if __name__ == "__main__":
    main()
