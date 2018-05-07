#!/usr/bin/env python3


def populate_array(rows, colls):
    array = [['.' for x in range(colls)] for y in range(rows)]
    for x in range(rows):
        for y in range(colls):
            if (x % 2 and not y % 2) or (not x % 2 and y % 2):
                array[x][y] = '*'
    return array


def main():
    try:
        rows_num, collumns_num = [int(i) for i in input(
            "Enter two integer numbers separated with spaces\n").split()]
    except ValueError:
        print("Try again using integer numbers only, thanks")
        exit()

    for row in populate_array(rows_num, collumns_num):
        print(*row)


if __name__ == "__main__":
    main()
