#!/usr/bin/env python3
"""Ladder"""


def main():
    """Main function"""
    number = int(input())

    for i in range(1, number + 1):
        for j in range(1, i + 1):
            print(j, sep='', end='')
        print()


if __name__ == '__main__':
    main()
