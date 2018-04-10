def diagonals(n, m):
    res = []
    for r in range(n):
        row = []
        for c in range(m):
            row += [abs(r-c)]
        res += [row]
    return res

def print_table(table):
    for r in range(len(table)):
        print(table[r])

print_table(diagonals(10,20))
