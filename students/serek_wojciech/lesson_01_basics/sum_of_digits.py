#!/usr/bin/env python3
"""Tens digit"""


def main():
    """Main function"""
    value = int(input())

    hundreds = value // 100
    dozens = value % 100 // 10
    units = value % 10

    print(hundreds + dozens + units)


if __name__ == '__main__':
    main()
