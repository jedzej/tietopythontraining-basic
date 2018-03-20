#!/usr/bin/env python3
"""The length of segment"""
import math


def distance(x_1, y_1, x_2, y_2):
    """Compute distance between two points"""
    return math.sqrt(math.pow(x_2 - x_1, 2) + math.pow(y_2 - y_1, 2))


def main():
    """Main function"""
    x_1 = float(input())
    y_1 = float(input())
    x_2 = float(input())
    y_2 = float(input())

    print(distance(x_1, y_1, x_2, y_2))


if __name__ == '__main__':
    main()
