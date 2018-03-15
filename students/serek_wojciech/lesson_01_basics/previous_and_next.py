#!/usr/bin/env python3
"""Previous and next"""


def main():
    """Main function"""
    number = int(input())

    print('The next number for the number {0} is {1}.'.
          format(number, number + 1))
    print('The previous number for the number {0} is {1}.'
          .format(number, number - 1))


if __name__ == '__main__':
    main()
