#!/usr/bin/env python3
"""Greater than neighbours exercise"""


def main():
    """Main function"""
    neighbours = [int(n) for n in input().split()]

    count = 0
    for idx in range(1, len(neighbours) - 1):
        if neighbours[idx - 1] < neighbours[idx] > neighbours[idx + 1]:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
