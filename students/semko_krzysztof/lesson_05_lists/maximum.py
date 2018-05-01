"""
Given two integers representing the rows and columns (m×n),
and subsequent m rows of n elements, find the index position
of the maximum element and print two numbers representing
the index (i×j) or the row number and the column number.
If there exist multiple such elements in different rows,
print the one with smaller row number. If there multiple
such elements occur on the same row, o
utput the smallest column number.
"""


def main():
    matrix = [int(x) for x in input().split()]

    rows, columns = matrix[0], matrix[1]

    max_coordinates = {0, 0}
    max_value = 0
    for i in range(rows):
        row = [int(x) for x in input().split()]

        for j in range(columns):
            if row[j] > max_value or i == 0 and j == 0:
                max_value = row[j]
                max_coordinates = i, j

    print(str(max_coordinates))


if __name__ == '__main__':
    main()
