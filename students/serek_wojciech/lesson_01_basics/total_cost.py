#!/usr/bin/env python3
"""Total cost"""


def main():
    """Main function"""
    price_dollars = int(input())
    price_cents = int(input())
    cups = int(input())

    total_dollars = cups * price_dollars + ((cups * price_cents) // 100)
    total_cents = (cups * price_cents) % 100

    print("{0} {1}".format(total_dollars, total_cents))


if __name__ == '__main__':
    main()
