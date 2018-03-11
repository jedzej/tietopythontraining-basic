#!/usr/bin/env python3
"""First digit after decimal"""


def main():
    """Main function"""
    value = float(input())

    print(int((value - int(value)) * 10))


if __name__ == '__main__':
    main()
