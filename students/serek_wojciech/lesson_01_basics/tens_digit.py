#!/usr/bin/env python3
"""Tens digit"""


def main():
    """Main function"""
    value = int(input())

    print((value % 100) // 10)


if __name__ == '__main__':
    main()
