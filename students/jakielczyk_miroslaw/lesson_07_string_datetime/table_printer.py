def print_table(table_data):
    columns_max_length = []
    for line in table_data:
        max_length = 0
        for word in line:
            if len(word) > max_length:
                max_length = len(word)
        columns_max_length.append(max_length)

    for x in range(len(table_data[0])):
        row_string = ''
        for y in range(len(table_data)):
            row_string += (table_data[y][x]).rjust(int(columns_max_length[y] + 2))
        print(row_string)


def main():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['dogs', 'cats', 'moose', 'goose']]

    print_table(table_data)


if __name__ == "__main__":
    main()
