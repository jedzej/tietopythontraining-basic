import re
import glob


def search_for_regex(searched_regex):
    for evry_file in glob.glob("*.txt"):
        file = open(evry_file)
        text = file.readlines()
        for line in text:
            check = searched_regex.search(line)
            if check is not None:
                print("Serched line is:\n " + line + "from file: " + evry_file)
        file.close()


regex = input("Give searched regex: ")
print("The searched regex is: " + regex)
searched_regex = re.compile(regex)
search_for_regex(searched_regex)
