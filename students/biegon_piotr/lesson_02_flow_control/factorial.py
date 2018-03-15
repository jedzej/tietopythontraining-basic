print("Factorial\n")

n = int(input("Enter a number: "))
factorial = 1

for i in range(2, n + 1):
    factorial = factorial * i

print("{:d}! = {:d}".format(n, factorial))
