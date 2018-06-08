import re
import os


prefix = "spam"
suffix = ".txt"
source = "/home/rybaapau/test"
pattern = re.compile(prefix + r'.*(\d{3})' + suffix)


def filling_the_gaps(folder):
    for foldername, subfolders, filenames in os.walk(folder):
        index = 0
        for filename in sorted(filenames):
            if pattern.match(filename):
                index += 1
                new_filename = prefix + str(index).zfill(3) + suffix

                print("Old: {}, new: {}".format(filename, new_filename))

                filename_path = os.path.join(foldername, filename)
                new_filename_path = os.path.join(foldername, new_filename)
                os.rename(filename_path, new_filename_path)


if __name__ == '__main__':
    filling_the_gaps(source)
    print('The end')
