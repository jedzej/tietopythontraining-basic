print("Ladder\n")

n = int(input("Enter a number less than or equal to 9: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, sep="", end="")
    print()
