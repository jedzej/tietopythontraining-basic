numberOfSteps = int(input("Enter number of steps: "))

for x in range(1, numberOfSteps + 1):
    for y in range(1, x + 1):
        print(y, sep='', end='')
    print()