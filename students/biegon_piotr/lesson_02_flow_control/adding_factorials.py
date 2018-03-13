print("Adding factorials\n")

n = int(input("Enter a number: "))
factorial = 1
s = 1

for i in range(2, n + 1):
    factorial = factorial * i
    s += factorial

print("Sum of factorials = {:d}".format(s))
