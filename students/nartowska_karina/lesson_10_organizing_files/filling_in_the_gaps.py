import re
import os


def filling_in_the_gaps():
    prefix = 'spam'
    suffix = '.txt'
    folder_path = '/home/user/Desktop/lesson_10_organizing_files/'
    regex = re.compile(prefix + r'.*(\d{3})' + suffix)
    tab = []
    new = []

    for folder, subfolders, files in os.walk(folder_path):
        for file in files:
            search = re.search(regex, file)
            if search is not None:
                tab.append(file)

    tab = sorted(tab)

    for i in range(len(tab)):
        if i < 9:
            new.append(prefix + '00' + str(i+1) + suffix)
        elif i >= 9 & i < 99:
            new.append(prefix + '0' + str(i+1) + suffix)
        else:
            new.append(prefix + str(i+1) + suffix)
    for i in range(len(tab)):
        if new[i] != tab:
            os.replace(tab[i], new[i])


def main():
    filling_in_the_gaps()


if __name__ == "__main__":
    main()
