table_data = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]


def func(table_data):
    col_widths = len(table_data)
    col_length = len(table_data[0])
    max_width = [0] * col_widths

    for j in range(col_length):
        for i in range(col_widths):
            if max_width[i] < len(table_data[i][j]):
                max_width[i] = len(table_data[i][j])

    for j in range(col_length):
        line = ''
        for i in range(col_widths):
            print(table_data[i][j].rjust(max_width[i]), " ", end='')
        print("")


def main():
    func(table_data)


if __name__ == "__main__":
    main()
