#!/usr/bin/env python3
"""Clock face"""


def main():
    """Main function"""
    hours = int(input())
    minutes = int(input())
    seconds = int(input())

    deg_per_sec = (12 * 60 * 60) / 360
    total_sec = (hours * 60 * 60) + (minutes * 60) + seconds

    print(total_sec / deg_per_sec)


if __name__ == '__main__':
    main()
