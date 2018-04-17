#!/usr/bin/env python3


def print_table(data_table):
    if not isinstance(data_table[0], list):
        col_width = 0
        for element in data_table:
            if not isinstance(element, str):
                element = str(element)
            col_width = max(len(element), col_width)

        for element in data_table:
            print(element.rjust(col_width))

    else:
        num_of_rows = len(data_table)
        num_of_cols = len(max(data_table, key=len))
        col_widths = [0] * num_of_rows

        for x, row in enumerate(data_table):
            for y, element in enumerate(row):
                if not isinstance(element, str):
                    data_table[x][y] = str(element)
                col_widths[x] = max(len(data_table[x][y]), col_widths[x])

            # complementing missing matrix elements if needed
            while len(row) < num_of_cols:
                row.append('')

        for y in range(num_of_cols):
            print(" ".join(data_table[x][y].rjust(col_widths[x]) for x
                           in range(num_of_rows)))


def main():
    table_data = [['oranges', 'cherries'],
                  ['Alice', 'Carol', 'David'],
                  [128, 512, 1024, '0x666'],
                  ['dogs', 'cats', 'moose', 'pigs']]

    print_table(table_data)


if __name__ == "__main__":
    main()
