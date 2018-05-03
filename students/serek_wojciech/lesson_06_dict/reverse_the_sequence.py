#!/usr/bin/env python3
"""Reverse the sequence"""


def reverse():
    """Revers order of user sequence"""
    value = int(input())
    if value:
        reverse()
    print(value)


def main():
    """Main function"""
    reverse()


if __name__ == '__main__':
    main()
