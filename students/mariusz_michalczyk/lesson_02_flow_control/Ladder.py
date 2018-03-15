top = int(input())
for level in range(1, top + 1):
    for item in range(1, level + 1):
        print(item, sep='', end='')
    print(end='\n')