#!/usr/bin/env python3


def comma_code(in_list):
    num_of_elements = len(in_list)

    if num_of_elements == 0:
        return ""
    if num_of_elements == 1:
        return in_list[0]

    out_str = ', '.join(in_list)
    last_comma = out_str.rfind(',')

    out_str = '{} and {}'.format(
        out_str[:last_comma], out_str[last_comma + 2:])

    return out_str


def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_code(spam))


if __name__ == "__main__":
    main()
