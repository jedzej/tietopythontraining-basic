number = int(input('Number: '))

total = 1
factorial_sum = 0
for x in range(1, number+1):
    total = total * x
    factorial_sum += total


print(factorial_sum)
