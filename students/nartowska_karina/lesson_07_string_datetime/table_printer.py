def print_table(table_data):
    col_widths = []
    for i in range(len(table_data)):
        max_len = 0
        for j in range(len(table_data[0])):
            if len(table_data[i][j]) > max_len:
                max_len = len(table_data[i][j])
        col_widths.append(max_len)

    for j in range(len(table_data[0])):
        tmp = 0
        for i in range(len(table_data)):
            print(table_data[i][j].rjust(col_widths[tmp]), end=" ")
            tmp += 1
        print()


def main():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    print("Result:")
    print_table(table_data)


if __name__ == '__main__':
    main()
