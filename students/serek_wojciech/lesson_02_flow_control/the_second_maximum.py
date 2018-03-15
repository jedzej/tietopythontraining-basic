#!/usr/bin/env python3
"""The second maximum"""


def main():
    """Main function"""
    first_max = -1
    sec_max = -1
    number = -1

    while number:
        number = int(input())
        if number > first_max:
            sec_max = first_max
            first_max = number
        elif number > sec_max:
            sec_max = number

    print(sec_max)


if __name__ == '__main__':
    main()
