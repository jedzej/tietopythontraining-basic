input_str = input()
n, m = map(int, input_str.split())
tab = [[0] * m for i in range(n)]
count = 0
for row in tab:
    for item in row:
        if count:
            item = '*'
        else:
            item = '.'
        print(item, end='')
        count = not count
    count = not count
    print()
