a = int(input())
for i in range(a):
    if i != 0:
        print()
    for j in range(a):
        print(abs(i - j), " ", end='')
