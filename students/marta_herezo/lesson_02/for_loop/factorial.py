# For the given integer n calculate the value n!

print('Give the integer number (n):')
n = int(input())

result = 1
for i in range(n):
    n = result * i
    result += n
print('The result is: ' + str(result))

