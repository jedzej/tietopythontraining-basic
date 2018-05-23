
def printTable(table):
    tab_len = len(table)
    str_num = len(table[0])
    colWidths = [0] * tab_len

    for i in range(tab_len):
        max_val = 0
        for _str in table[i]:
            max_val = max(len(_str), max_val)
        colWidths[i] = max_val

    for i in range(str_num):
        for j in range(tab_len):
            print(table[j][i].rjust(colWidths[j]), end=' ')
        print('')


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)
