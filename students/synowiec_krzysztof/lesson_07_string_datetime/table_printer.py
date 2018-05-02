def main():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['dogs', 'cats', 'moose', 'goose']]
    print_table(table_data)


def print_table(table_data):
    col_width = []
    for parts in table_data:
        longest_string = 0
        for item in parts:
            length = len(item)
            if length > longest_string:
                longest_string = length
        col_width.append(longest_string)

    for x in range(len(table_data[0])):
        for y in range(len(table_data)):
            print(table_data[y][x].rjust(col_width[y]), end=" ")
        print()


if __name__ == '__main__':
    main()
