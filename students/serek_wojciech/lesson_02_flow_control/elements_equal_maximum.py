#!/usr/bin/env python3
"""The number of elements equal to the maximum"""


def main():
    """Main function"""
    max_value = -1
    max_count = -1
    number = -1

    while number:
        number = int(input())
        if number > max_value:
            max_value = number
            max_count = 1
        elif number == max_value:
            max_count += 1

    print(max_count)


if __name__ == '__main__':
    main()
