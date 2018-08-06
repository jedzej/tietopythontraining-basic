import os
import re

prefix = "spam"
pattern = re.compile(prefix + r'.*(\d{3})')


def fill_the_gaps(folder):
    for foldername, subfolders, filenames in os.walk(folder):
        filenames = sorted(filenames)
        index = 1
        new_filename = ''
        for filename in filenames:
            if pattern.match(filename):
                if index == 1:
                    new_filename = re.sub(r'\d{3}', '001', filename)
                print(filename, new_filename, index)
                if filename != new_filename:
                    print(
                        "Missing filename: " + new_filename + "\nFile " +
                        filename + " will be renamed.")
                    filename_path = os.path.join(foldername, filename)
                    new_filename_path = os.path.join(foldername, new_filename)
                    os.rename(filename_path, new_filename_path)
                new_filename = filename.replace(str(index), str(index + 1))
                index += 1


if __name__ == '__main__':
    fill_the_gaps(".\gaps")
