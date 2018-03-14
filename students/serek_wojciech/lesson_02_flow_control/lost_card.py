#!/usr/bin/env python3
"""Lost card"""
import math


def main():
    """Main function"""
    cards = int(input())
    sum_of_cards = int(math.fsum(range(cards + 1)))

    for i in range(cards - 1):      # pylint: disable=unused-variable
        sum_of_cards -= int(input())

    print(sum_of_cards)


if __name__ == '__main__':
    main()
