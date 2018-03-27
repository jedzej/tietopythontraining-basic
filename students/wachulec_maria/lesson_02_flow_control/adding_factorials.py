n = int(input("n: "))
factorial = 1
result = 0
for i in range(1, n + 1):
    factorial *= i
    result += factorial
print(result)
