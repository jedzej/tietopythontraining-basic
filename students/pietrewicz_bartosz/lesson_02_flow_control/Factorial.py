# Read an integer n
n = int(input())
# Calculate the factorial of n if n >= 0
if n < 0:
    print("Enter a number >= 0")
else:
    result = 1
    for i in range(2, n+1):
        result *= i
    print(result)
