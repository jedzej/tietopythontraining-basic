def print_table(list_of_lists_of_strings):
    col_widths = []
    for list_of_strings in list_of_lists_of_strings:
        max_string = 0
        for item in list_of_strings:
            if len(item) > max_string:
                max_string = len(item)
        col_widths.append(max_string)

    for row in range(len(list_of_lists_of_strings[0])):
        for col in range(len(list_of_lists_of_strings)):
            print(list_of_lists_of_strings[col][row].rjust(col_widths[col]),
                  end=" ")

        print()


def main():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['dogs', 'cats', 'moose', 'goose']]

    print_table(table_data)


if __name__ == '__main__':
    main()
