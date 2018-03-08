print("The number of zeros\n")

N = int(input("Enter the number of numbers: "))
result = 0

for i in range(1, N + 1):
    a = int(input("Enter a number: "))
    if a == 0:
        result += 1

print("\nYou have entered {:d} numbers equal to 0".format(result))
