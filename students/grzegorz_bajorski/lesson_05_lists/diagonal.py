def diagonal(n):
    table = []

    for i in range(n):
        table.append([])
        for j in range(n):
            table[i].append(abs(i - j))
            print(table[i][j], end=' ')
        print("")


diagonal(int(input()))
