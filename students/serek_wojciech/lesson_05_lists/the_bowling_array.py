#!/usr/bin/env python3
"""The bowling array exercise"""


def main():
    """Main function"""

    pins_value, balls_value = [int(i) for i in input().split()]
    pins = ['I'] * pins_value

    for _ in range(balls_value):
        left, right = [int(i) for i in input().split()]
        for pin in range(left - 1, right):
            pins[pin] = '.'

    print(''.join(pins))


if __name__ == '__main__':
    main()
