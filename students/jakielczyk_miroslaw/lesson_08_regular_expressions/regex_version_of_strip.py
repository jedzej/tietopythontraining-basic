import re


def strip_by_regex(*args):
    if len(args) == 1:
        strip_regex = re.compile(r'^\s+|\s+$')
        string_after_regex = strip_regex.sub('', args[0])
        print("String before strip-regex:***", args[0], "***",
              "\nString after strip-regex operation:***", string_after_regex, "***")
    elif len(args) == 2:
        remove_characters_regex = re.compile(args[1])
        string_after_regex = remove_characters_regex.sub('', args[0])
        print("String before regex:***", args[0], "***",
              "\nString after regex operation:***", string_after_regex, "***")


def main():
    text = "  one _two! three   four, one tw o three four, one two !!!+= three four !  "
    strip_by_regex(text)
    strip_by_regex(text, "two")


if __name__ == "__main__":
    main()
