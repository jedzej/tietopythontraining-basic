#!/usr/bin/env python3
"""The Collatz Sequence"""


def collatz(value):
    """Calculate next Collatz Sequence element"""
    if value % 2:  # odd number
        result = 3 * value + 1
    else:
        result = value // 2

    print(result)
    return result


def main():
    """Main function"""
    try:
        value = abs(int(input()))
        while value != 1:
            value = collatz(value)
    except ValueError:
        print("Integer value must be enter!")


if __name__ == '__main__':
    main()
