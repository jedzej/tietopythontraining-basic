number = int(input('Give the number: '))

factorial = 1
result = 0
for x in range(1, number + 1):
    factorial *= x
    result += factorial

print('{} {}'.format('Result:', result))
