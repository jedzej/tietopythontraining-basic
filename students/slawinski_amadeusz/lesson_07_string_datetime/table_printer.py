#!/usr/bin/env python3


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    max_in_subtable = []

    for subtable in table:
        max_in_subtable.append(0)
        for element in subtable:
            max_in_subtable[-1] = max(max_in_subtable[-1], len(element))

    for i in range(len(table[0])):
        j = 0
        for subtable in table:
            print(subtable[i].rjust(max_in_subtable[j]), end=' ')
            j = j + 1
        print()


if __name__ == "__main__":
    printTable(tableData)
