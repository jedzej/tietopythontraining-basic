#!/usr/bin/env python3


def populate_symmetric_matrix(m):
    array = [[None] * m for y in range(m)]
    for x in range(m):
        for y in range(m):
            array[x][y] = abs(x - y)
    return array


def main():
    try:
        input_number = int(input("Enter integer number\n"))
    except ValueError:
        print("Try again using integer number only, thanks")
        exit()

    for row in populate_symmetric_matrix(input_number):
        print(*row)


if __name__ == "__main__":
    main()
