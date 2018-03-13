ladder = int(input())
for j in range(1, ladder+1):
    for i in range(1, j+1):
        print(i, end='')
    print(sep='\n')
