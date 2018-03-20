steps = int(input())
row = ""

if steps <= 9:
    for i in range(1, steps + 1):
        row += str(i)
        print(row, sep="")
else:
    print("Number of steps must be max 9")
