number = int(input())

sum = 0
for s in range(1, number + 1):
    factorial = 1
    for f in range(1, s + 1):
        factorial *= f
    sum += factorial

print(sum)
