print('For a given integer, \
print the sum of factorials')
number = int(input('Enter a number: '))
sumoffact = 0
factorial = 1
for i in range(1, number + 1):
    factorial = factorial * i
    sumoffact += factorial
print('The sum of factorials is: ' + str(sumoffact))
