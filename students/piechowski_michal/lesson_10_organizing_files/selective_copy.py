#!/usr/bin/env python3

import glob
import os
import shutil


def main():
    dir_path = "new_folder/"
    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)
    os.mkdir(dir_path)

    for extension in (".pdf", ".txt"):
        for path in glob.glob("./**/*" + extension, recursive=True):
            shutil.copy2(path, dir_path)


if __name__ == "__main__":
    main()
