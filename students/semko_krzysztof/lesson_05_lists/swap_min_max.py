"""
Given a list of unique numbers, swap the minimal
and maximal elements of this list. Print the resulting list.
"""


def main():
    tab = [int(tab) for tab in input().split()]

    min_index = tab.index(min(tab))
    max_index = tab.index(max(tab))

    tab[min_index], tab[max_index] = tab[max_index], tab[min_index]
    print(' '.join(str(i) for i in tab))


if __name__ == '__main__':
    main()
