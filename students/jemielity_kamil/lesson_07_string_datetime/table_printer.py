def print_table(data):
    col_width = []
    for i in range(len(data)):
        maximum = 0
        for j in range(len(data[0])):
            if len(data[i][j]) > maximum:
                maximum = len(data[i][j])
        col_width.append(maximum)

    for j in range(len(data[0])):
        counter = 0
        for i in range(len(data)):
            print(data[i][j].rjust(col_width[counter]), end=" ")
            counter += 1
        print()


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

print_table(tableData)
