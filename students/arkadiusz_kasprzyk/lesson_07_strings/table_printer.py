# table_printer.py

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table, sep=' ', fill=' '):
    """
    Example
    -------
    printTable(tableData)
    printTable(tableData, sep='  ')
    printTable(tableData, sep='...')
    printTable(tableData, sep='...', fill='.')
    """

    col_widths = []
    for k in range(len(table)):
        lengths = []
        for s in table[k]:
            lengths.append(len(s))
        col_widths.append(max(lengths))

    for r in range(len(lengths)):       # rows
        for c in range(len(table)):     # columns
            print(table[c][r].ljust(col_widths[c], fill), end=sep)
        print()
