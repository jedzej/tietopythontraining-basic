table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def get_biggest_len(col):
    bgst_len = 0
    for item in col:
        if len(item) > bgst_len:
            bgst_len = len(item)
    return bgst_len


def print_table(table_data):
    col_width = len(table_data[0])
    for i in range(col_width):
        for col in table_data:
            bgst_len = get_biggest_len(col)
            print(str(col[i]).rjust(bgst_len), end=' ')
        print('')


if __name__ == '__main__':
    print_table(table_data)
