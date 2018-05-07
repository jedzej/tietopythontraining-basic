n = int(input())
for x in range(n):
    row = []
    for y in range(n):
        row.append(str(abs(y - x)))
    print(' '.join(row))
