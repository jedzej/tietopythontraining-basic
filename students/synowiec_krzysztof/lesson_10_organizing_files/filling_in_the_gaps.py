import os
import re
import shutil


BASE_DIR = "original"
PREFIX = "spam"


def main():
    files = [file for file in os.listdir(BASE_DIR) if file.startswith(PREFIX)]
    print(files)
    files.sort()
    print(files)
    pattern = re.compile(r'\d{3}')

    if len(files) > 2:
        prev_n = None
        gap_found = False
        for file in files:
            curr_n = int(pattern.search(file).group())
            print("current {}".format(curr_n))
            if not gap_found:
                if prev_n is not None and prev_n + 1 != curr_n:
                    gap_found = True
            if gap_found:
                curr_n = prev_n + 1
                corr_file = re.sub(r'\d{3}', '{0:0>3}'.format(curr_n), file)
                old_path = os.path.join(BASE_DIR, file)
                new_path = os.path.join(BASE_DIR, corr_file)
                shutil.move(old_path, new_path)
            prev_n = curr_n


if __name__ == '__main__':
    main()
