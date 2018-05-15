# The program print that is possible to split k bars in one move

n = int(input("Put number of bar in vertical: "))
m = int(input("Put number of bar in vertical: "))
k = int(input("Put number of bar that you want: "))

power_1 = (k / n) % 1
power_2 = (k / m) % 1

if (k <= (m * n)) & ((power_1 == 0) or (power_2 == 0)):
    value = "YES"
else:
    value = "NO"

print("\nOr is possible to split k bars in one move?:", value)
