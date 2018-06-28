# Given an integer n, print the sum 1!+2!+3!+...+n!
print('Enter the number of factorials to add up: ')
n = int(input())
factorial = 1
result = 0

for i in range(1, n + 1):
    factorial *= i
    result += factorial

print('Result = ' + str(int(result)))
