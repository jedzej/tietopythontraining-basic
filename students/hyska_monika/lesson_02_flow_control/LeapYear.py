# The program print that year is leap

y = int(input("Put year: "))

l1 = (y / 400) % 1
l2 = (y / 4) % 1
l3 = (y / 100) % 1

if (l1 == 0) or ((l2 == 0) & (l3 != 0)):
    value = "LEAP"
else:
    value = "COMMON"

print("\nWhat type is year?:", value)
