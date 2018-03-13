#!/usr/bin/env python3
"""Knight move"""


def main():
    """Main function"""
    start_x = int(input())
    start_y = int(input())
    new_x = int(input())
    new_y = int(input())

    if abs(start_x - new_x) == 2 and abs(start_y - new_y) == 1 or \
       abs(start_y - new_y) == 2 and abs(start_x - new_x) == 1:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
