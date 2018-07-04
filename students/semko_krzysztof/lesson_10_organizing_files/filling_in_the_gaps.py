"""
Write a program that finds all files with a given prefix,
such as spam001.txt, spam002.txt, and so on,
in a single folder and locates any gaps in the numbering
(such as if there is a spam001.txt and spam003.txt but no
spam002.txt). Have the program rename all the later files
to close this gap.

As an added challenge, write another program that can
insert gaps into numbered files so that a new file
can be added.
"""

import os
import shutil


def remove_gaps(directory, prefix):
    files = os.listdir(directory)

    if len(files) == 0:
        return

    last_number = int(get_string_number(files[0], prefix))
    for file_name in files:
        current_str_number = int(get_string_number(file_name, prefix))
        if current_str_number != last_number:
            src = os.path.join(directory, file_name)
            dst = os.path.join(directory,
                               prefix + '{0:03d}'.format(last_number + 1) +
                               get_extension(file_name))
            last_number += 1
            shutil.move(src, dst)


def get_string_number(file_name, prefix):
    ext = file_name.find(".")
    number = file_name[len(prefix):ext]
    return number


def get_extension(name):
    return name[name.find("."):]


def main():
    gaps_dir = os.path.join(os.getcwd(), "filling_gaps")
    remove_gaps(gaps_dir, "spam_")


if __name__ == '__main__':
    main()
