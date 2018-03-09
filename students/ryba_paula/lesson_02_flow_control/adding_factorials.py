n = int(input())

factorial = 1
result = 0

for i in range(1, n + 1):
    factorial = factorial * i
    result = result + factorial
    
print(result)