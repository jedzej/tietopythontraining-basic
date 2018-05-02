def print_table(table_data):
    col_widths = [0] * len(table_data)
    for i, data in enumerate(table_data):
        col_widths[i] = len(max(data, key=len))
    for s in zip(*table_data):
        print(' '.join(text.rjust(col_widths[i]) for i, text in enumerate(s)))


if __name__ == '__main__':
    test_data = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]
    print_table(test_data)
