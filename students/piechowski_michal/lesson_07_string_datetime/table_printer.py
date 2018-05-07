#!/usr/bin/env python3


def printTable(list_of_lists):
    max_lengths = {}

    for single_list in list_of_lists:
        for i in range(0, len(single_list)):
            max_lengths[i] = max(max_lengths.get(i, -1), len(single_list[i]))

    for single_list in list_of_lists:
        for i in range(0, len(single_list)):
            print(single_list[i].rjust(max_lengths[i]), end=" ")
        print("")


def main():
    tableData = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    printTable(tableData)


if __name__ == "__main__":
    main()
