import re


def main():
    text_example = "      text_1 and text_2    "
    remove_text = "te"
    print(custom_strip(text_example))
    print(custom_strip(text_example, remove_text))


def custom_strip(string, remove=""):
    """clean begin and end of string"""
    regex_clean_func = re.compile(r'^\s+|\s+$')
    string_striped = regex_clean_func.sub('', string)
    """remove argument from string"""
    regex_arg_remove = re.compile(remove)
    return regex_arg_remove.sub('', string_striped)


if __name__ == '__main__':
    main()
