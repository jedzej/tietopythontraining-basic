def printTable(table_data):
    col_w = len(table_data)
    col_l = len(table_data[0])
    max_w = [0] * col_w

    for j in range(col_l):
        for i in range(col_w):
            if max_w[i] < len(table_data[i][j]):
                max_w[i] = len(table_data[i][j])

    for j in range(col_l):
        for i in range(col_w):
            print(table_data[i][j].rjust(max_w[i]), " ", end='')
        print("")


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)