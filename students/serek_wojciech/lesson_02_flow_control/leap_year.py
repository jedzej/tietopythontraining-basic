#!/usr/bin/env python3
"""Leap year"""


def main():
    """Main function"""
    year = int(input())

    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print('LEAP')
    else:
        print('COMMON')


if __name__ == '__main__':
    main()
