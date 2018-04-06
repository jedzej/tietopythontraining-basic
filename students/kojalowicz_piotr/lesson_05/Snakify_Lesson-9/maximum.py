def main():
    param_table = input().split()
    rows = int(param_table[0])
    columns = int(param_table[1])
    table = []
    max_row = 0
    maxi = None
    for row in range(rows):
        table.append([0]*columns)
    for row in range(rows):
        row_elemnts = input().split()
        for column in range(columns):
            table[row][column] = int(row_elemnts[column])
            if row == 0 and column == 0:
                maxi = table[row][column]
            if maxi < table[row][column]:
                maxi = table[row][column]
                max_row = row
    max_column = table[max_row].index(max(table[max_row]))
    print(str(max_row) + " " + str(max_column))


if __name__ == '__main__':
    main()
