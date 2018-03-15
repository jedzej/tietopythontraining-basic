#!/usr/bin/env python3
"""Knight move"""


def main():
    """Main function"""
    n = int(input())
    m = int(input())
    k = int(input())

    if k <= m * n and (k % m == 0 or k % n == 0):
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
