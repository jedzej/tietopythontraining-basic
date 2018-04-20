tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def print_table(table_data):
    new_row = []
    for i in range(len(table_data[0])):
        new_row.append("")
        for j in range(len(table_data)):
             new_row[i] += table_data[j][i] + ' '
    for i in new_row:
        print(i)

print_table(tableData)

