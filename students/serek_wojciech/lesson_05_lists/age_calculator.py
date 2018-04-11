#!/usr/bin/env python3
"""Age calculator exercise"""


def main():
    """Main function"""
    people = [int(item) for item in input().split()]
    children = [item for item in people if item < 18]
    adults = [item for item in people if item > 18]

    try:
        print("Adults average: " + str(sum(adults) / len(adults)))
    except ZeroDivisionError:
        print("No adults")
    print("Number of children: " + str(len(children)))


if __name__ == '__main__':
    main()
