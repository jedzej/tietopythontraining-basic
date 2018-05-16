import re


def version_of_strip(text, characters=" "):
    r_text = re.compile("^([" + characters + "]*)|([" + characters + "]*)$")
    print(r_text.sub("", text))


def main():
    version_of_strip("  no char, only text  ")
    version_of_strip("one char a b c", "on")
    version_of_strip("   two chars a o c b", "c b")


if __name__ == "__main__":
    main()
