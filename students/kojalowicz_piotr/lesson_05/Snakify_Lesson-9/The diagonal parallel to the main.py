def main():
    size = int(input())
    table = []
    for line in range(size):
        table.append([0] * size)
    for row in range(size):
        for column in range(size):
            table[row][column] = abs(column - row)
    graf = ''
    for row in range(size):
        for column in range(size):
            graf += str(table[row][column]) + ' '
        graf += '\n'
    print(graf)


if __name__ == '__main__':
    main()
