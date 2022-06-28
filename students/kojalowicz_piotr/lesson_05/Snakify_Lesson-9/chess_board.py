def main():
    param_table = input().split()
    rows = int(param_table[0])
    columns = int(param_table[1])
    table = []
    for row in range(rows):
        table.append([0] * columns)
    for row in range(rows):
        for column in range(columns):
            if (row + column) % 2 == 0:
                table[row][column] = '. '
            else:
                table[row][column] = '* '
    graf = ''
    for row in range(rows):
        for column in range(columns):
            graf += table[row][column]
        graf += '\n'
    print(graf)


if __name__ == '__main__':
    main()
