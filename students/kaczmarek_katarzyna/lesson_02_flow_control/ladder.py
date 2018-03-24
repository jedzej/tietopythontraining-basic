steps = int(input("Number of steps (1-9): "))
row = ""

if 0 < steps <= 9:
    for i in range(1, steps + 1):
        row += str(i)
        print(row, sep='')
else:
    print("Wrong number of steps. Valid range: 1-9")
