# Given two integers representing the rows and columns (m×n), and subsequent
#  m rows of n elements, find the index position of the maximum element and
# print two numbers representing the index (i×j) or the row number and the
# column number. If there exist multiple such elements in different rows,
# print the one with smaller row number. If there multiple such elements
# occur on the same row, output the smallest column number.


def find_maximum(table):
    row_maxes = []
    row_maxes_idx = []

    for row in table:
        row_maxes_idx.append(row.index(max(row)))
        row_maxes.append(max(row))

    row_position = row_maxes.index(max(row_maxes))
    column_position = row_maxes_idx[row_position]

    return row_position, column_position


def init_table(table):
    rows_size, columns_size = (
        int(a) for a in input('Enter the rows and columns (m×n): ').split())

    for i in range(rows_size):
        row_input = input().split(' ')
        converted_row = [int(x) for x in row_input]
        table.append(converted_row)
    return table


def main():
    table = []
    row, column = find_maximum(init_table(table))
    print(str(row) + " x " + str(column))


if __name__ == "__main__":
    main()
