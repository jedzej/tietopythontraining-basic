x, y = [int(s) for s in input().split()]
for i in range(x):
    if i != 0:
        print()
    for j in range(y):
        if (i + j) % 2 == 1:
            print("* ", end='')
        else:
            print(". ", end='')
