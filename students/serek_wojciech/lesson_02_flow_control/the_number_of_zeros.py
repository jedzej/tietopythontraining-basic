#!/usr/bin/env python3
"""The number of zeros"""


def main():
    """Main function"""
    count = int(input())
    zeros = 0

    while count:
        count -= 1
        value = int(input())
        if not value:
            zeros += 1

    print(zeros)


if __name__ == '__main__':
    main()
