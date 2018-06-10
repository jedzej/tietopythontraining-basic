import os
import shutil

SOURCE_FOLDER = "source_folder"
DESTINATION_FOLDER = "destination_folder"


def create_test_file(filename):
    with open(filename, "w") as test_file:
        test_file.write("Test...")


def create_test_tree():
    if os.path.exists(SOURCE_FOLDER):
        shutil.rmtree(SOURCE_FOLDER)
    os.mkdir(SOURCE_FOLDER)
    if os.path.exists(DESTINATION_FOLDER):
        shutil.rmtree(DESTINATION_FOLDER)
    os.mkdir(DESTINATION_FOLDER)

    test1 = os.path.join(SOURCE_FOLDER, "test1")
    test2 = os.path.join(SOURCE_FOLDER, "test2", "test2_1")
    os.makedirs(test1)
    os.makedirs(test2)

    create_test_file(os.path.join(SOURCE_FOLDER, "root_test1.jpg"))
    create_test_file(os.path.join(SOURCE_FOLDER, "root_test2.jpg"))
    create_test_file(os.path.join(SOURCE_FOLDER, "root_test3.gif"))
    create_test_file(os.path.join(test1, "test1_test1.txt"))
    create_test_file(os.path.join(test1, "test1_test2.jpg"))
    create_test_file(os.path.join(test1, "test1_test3.pdf"))
    create_test_file(os.path.join(test2, "test2_test1.pdf"))
    create_test_file(os.path.join(test2, "test2_test2.jpg"))
    create_test_file(os.path.join(test2, "test2_test3.doc"))


def main():
    create_test_tree()

    for folder_name, _, file_names in os.walk(SOURCE_FOLDER):
        for filename in file_names:
            if filename.endswith((".jpg", ".pdf")):
                file_path = os.path.join(folder_name, filename)
                print(file_path)
                shutil.copy(file_path, DESTINATION_FOLDER)


if __name__ == "__main__":
    main()
