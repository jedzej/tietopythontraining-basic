# Given an integer n, print the sum 1!+2!+3!+...+n!
print('Enter the number of factorials to add up: ')
n = int(input())
factorial = 1
sum = 0

for i in range(1, n + 1):
    factorial = factorial * i
    sum += factorial

print('Result = ' + str(int(sum)))
