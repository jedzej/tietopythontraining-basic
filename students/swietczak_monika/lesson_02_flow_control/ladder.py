n = int(input("How many steps? "))

for k in range(1, n + 1):
    for l in range(1, k + 1):
        print(l, sep='', end='')
    print('\n')
