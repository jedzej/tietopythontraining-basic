#!/usr/bin/env python3
"""The diagonal parallel to the main exercise"""


def main():
    """Main function"""

    size = int(input())

    for row in range(size):
        for col in range(size):
            print(str(abs(row - col)) + ' ', end='')
        print('')


if __name__ == '__main__':
    main()
