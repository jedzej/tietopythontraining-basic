"""In mathematics, the factorial of an integer n, denoted by n! is
the following product: n!=1×2×…×n

For the given integer n
calculate the value n!. Don't use math module in this exercise. """

# Read an integer:
n = int(input())
f = 1
# Print a value:
for x in range(2, n + 1):
    f = f * x
print(f)
