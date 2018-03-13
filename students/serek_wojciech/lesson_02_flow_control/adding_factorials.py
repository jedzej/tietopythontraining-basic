#!/usr/bin/env python3
"""Adding factorials"""


def main():
    """Main function"""
    number = int(input())
    fact = 1
    fact_sum = 0

    for i in range(1, number + 1):
        fact *= i
        fact_sum += fact

    print(fact_sum)


if __name__ == '__main__':
    main()
