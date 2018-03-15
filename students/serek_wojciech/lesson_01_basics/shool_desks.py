#!/usr/bin/env python3
"""School desks"""


def main():
    """Main function"""
    group_a = int(input())
    group_b = int(input())
    group_c = int(input())

    desks_for_a = (group_a // 2) + (group_a % 2)
    desks_for_b = (group_b // 2) + (group_b % 2)
    desks_for_c = (group_c // 2) + (group_c % 2)

    print(desks_for_a + desks_for_b + desks_for_c)


if __name__ == '__main__':
    main()
