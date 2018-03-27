n = int(input())
k = int(input())

result = k // n
if k % n > 0:
    result = result + 1

print("Result: " + str(result))
