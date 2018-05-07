print('Enter a number: ')
givenint = int(input())
factor = 1
for i in range(1, givenint + 1):
    factor *= i
print(factor)
