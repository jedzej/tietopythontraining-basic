"""
Given a list of numbers, determine and print the quantity
of elements that are greater than both of their neighbors.

The first and the last items of the list shouldn't
be considered because they don't have two neighbors.
"""


def main():
    tab = [int(tab) for tab in input().split()]

    if len(tab) < 2:
        print(str(0))
        return

    number = 0
    for i in range(1, len(tab) - 1):
        if tab[i] > tab[i - 1] and tab[i] > tab[i + 1]:
            number += 1

    print(str(number))


if __name__ == '__main__':
    main()
