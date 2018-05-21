#!/usr/bin/env python3


def comma_code(list):
    num_of_elements = len(list)
    out_string = ''

    if num_of_elements > 1:
        for i in range(num_of_elements - 1):
            out_string += list[i] + ', '

        out_string = out_string[:-2] + ' and ' + list[num_of_elements - 1]

    elif num_of_elements > 0:
        out_string = list[0]

    return out_string


def main():
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_code(spam))


if __name__ == "__main__":
    main()
