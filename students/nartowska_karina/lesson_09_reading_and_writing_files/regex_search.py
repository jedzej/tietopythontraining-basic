import re
import glob


def search_regex(regex_search):
    for file in glob.glob("*.txt"):
        current = open(file)
        content = current.readlines()
        for line in content:
            if regex_search.match(line):
                print("Correct line is:\n" + line + "from file: " + file)

        current.close()


def main():
    reg = str(input("Give regex: "))
    print("Searching regex in .txt files: " + reg)
    regex_search = re.compile(reg)
    search_regex(regex_search)


if __name__ == "__main__":
    main()
