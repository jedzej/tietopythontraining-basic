#!/usr/bin/env python3
"""Maximum exercise"""


def main():
    """Main function"""

    rows, columns = [int(i) for i in input().split()]
    matrix = []

    for _ in range(rows):
        matrix.append([int(i) for i in input().split()])

    row_max = col_max = 0
    max_val = matrix[row_max][col_max]

    for row in range(rows):
        for col in range(columns):
            if matrix[row][col] > max_val:
                max_val = matrix[row][col]
                row_max = row
                col_max = col

    print(str(row_max) + ' ' + str(col_max))


if __name__ == '__main__':
    main()
