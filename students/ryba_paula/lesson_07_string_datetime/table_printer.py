def print_table(list_of_strings):
    col_widths = []
    for i in list_of_strings:
        max_string = 0
        for j in i:
            if len(j) > max_string:
                max_string = len(j)
        col_widths.append(max_string)

    for i in range(len(list_of_strings[0])):
        for j in range(len(list_of_strings)):
            print(list_of_strings[j][i].rjust(col_widths[j]), end=" ")

        print()


def main():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                 ['Alice', 'Bob', 'Carol', 'David'],
                 ['dogs', 'cats', 'moose', 'goose']]

    print_table(table_data)


if __name__ == '__main__':
    main()
