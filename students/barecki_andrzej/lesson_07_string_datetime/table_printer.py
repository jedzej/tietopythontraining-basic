""""
Notification:
Print result is without change raw and columns- "print just like I saw table"
I can fix that according specification if it is necessary.
"""


def main():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    print_table(table_data)


def print_table(data_list):

    """"Find the longest string in each column"""
    row_len = len(data_list)
    column_len = len(data_list[0])
    all_column_length = [0 for _ in range(column_len)]
    for column in range(column_len):
        single_column_length = [0 for _ in range(row_len)]
        for raw in range(row_len):
            single_column_length[raw] = len(data_list[raw][column])
        all_column_length[column] = max(single_column_length)

    """"Print table with each column right-justified"""
    for row in range(row_len):
        print(' '.join(data_list[row][column].rjust(all_column_length[column])
                       for column in range(column_len)))


if __name__ == '__main__':
    main()
