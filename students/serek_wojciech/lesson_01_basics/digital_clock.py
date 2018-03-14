#!/usr/bin/env python3
"""Digital clock"""


def main():
    """Main function"""
    minutes = int(input())

    print("{0} {1}".format(minutes // 60, minutes % 60))


if __name__ == '__main__':
    main()
