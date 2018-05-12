# In mathematics, the factorial of an integer n, denoted by n! is the following product:
# n!=1×2×…×n
# For the given integer n calculate the value n!. Don't use math module in this exercise.

# Read an integer:
a = int(input())
# Print a value:
fctr = 1
for i in range (2, a+1):
    fctr *= i
print(fctr)