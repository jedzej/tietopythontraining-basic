def getColWidths(tableData):
    col_widths = [0] * len(tableData)
    for i in range(len(tableData)):
        max = len(tableData[i][0])
        for j in range(len(tableData[0])):
            if len(tableData[i][j]) > max:
                max = len(tableData[i][j])
        col_widths[i] = max
    return col_widths


def printTable(tableData):
    col_widths = getColWidths(tableData)
    for i in range(len(tableData[0])):
        text = ''
        for j in range(len(tableData)):
            text += tableData[j][i].rjust(col_widths[j] + 1)
        print(text)


tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
print(printTable(tableData))
