#!/usr/bin/env python3


def index_of_maximum(array):
    max_element = array[0][0]

    for row in array:
        for element in row:
            max_element = max(max_element, element)

    for i, row in enumerate(array):
        for j, element in enumerate(row):
            if element == max_element:
                return i, j


def main():
    try:
        rows, collumns = [int(i) for i in input(
            "Enter two integer numbers separated with spaces\n").split()]
        user_array = [[int(j) for j in input(
            "Enter {} numbers separated with spaces\n"
            .format(collumns)).split()] for i in range(rows)]
    except IndexError:
        print("Try again: two numbers separated with spaces, then hit enter")
        exit()
    except ValueError:
        print("Try again using integer numbers only, thanks")
        exit()

    print(*index_of_maximum(user_array))


if __name__ == "__main__":
    main()
