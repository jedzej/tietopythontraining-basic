steps = int(input())

if steps <= 9:
    for i in range(1, steps + 1):
        for k in range(1, i + 1):
            print(k, sep='', end='')
        print()
else: 
    print("Number of steps must be max 9")