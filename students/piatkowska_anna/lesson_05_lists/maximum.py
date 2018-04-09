'''
Given two integers representing the rows and columns (m×n),
and subsequent m rows of n elements, find the index position
of the maximum element and print two numbers representing
the index (i×j) or the row number and the column number.
If there exist multiple such elements in different rows,
print the one with smaller row number.
If there multiple such elements occur on the same row,
output the smallest column number.
'''


def max_position():
    rows, column = [int(s)
                    for s in input("Enter row and column count:").split()]
    a = []
    max_row_index = 0
    max_col_index = 0
    for i in range(rows):
        a.append([int(s) for s in input("Enter row values: ").split()])
    for i in range(rows):
        for j in range(len(a[i])):
            if a[i][j] > a[max_row_index][max_col_index]:
                max_row_index = i
                max_col_index = j
    print("Index of maximum number in matrix is:",
          max_row_index, max_col_index)


if __name__ == "__main__":
    try:
        max_position()
    except ValueError:
        print("Invalid input")
