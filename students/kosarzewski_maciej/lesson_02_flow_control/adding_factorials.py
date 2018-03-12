total = 0
factorial = 1
a = int(input())
# Print a value:
for i in range(1, a+1):
    factorial *= i
    total += factorial
print(total)
