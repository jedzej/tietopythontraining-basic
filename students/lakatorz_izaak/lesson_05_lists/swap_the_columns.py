# Given two positive integers m and n, m lines of n elements, giving an m×n
# matrix A, followed by two non-negative integers i and j less than n,
# swap columns i and j of A and print the result.


def init_table(table):
    rows_size, columns_size = (
        int(a) for a in input('Enter the rows and columns (m×n): ').split())

    for i in range(rows_size):
        row_input = input().split(' ')
        converted_row = [int(x) for x in row_input]
        table.append(converted_row)

    return table


def swap_columns(a, i, j):
    for idx in range(len(a)):
        a[idx][i], a[idx][j] = a[idx][j], a[idx][i]
    return a


def main():
    table = []
    table = init_table(table)

    column_i, column_j = (
        int(a) for a in input().split())

    result_table = swap_columns(table, column_i, column_j)

    for row in range(len(result_table)):
        print(result_table[row])


if __name__ == "__main__":
    main()
