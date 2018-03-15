# Read an integer:
n = int(input())
# Print the sum of factorials from 1 up to n
if n <= 0:
    print("Enter a number > 0")
else:
    factorial_sum = 0
    current_factorial = 1
    for i in range(1, n+1):
        current_factorial *= i
        factorial_sum += current_factorial
    print(factorial_sum)
