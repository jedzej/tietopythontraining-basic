print('How many integers you want to check? ')
numofint = int(input())
zeros = 0
print('Enter ' + str(numofint) + ' numbers: ')
for i in range(numofint):
    print('Number ' + str(i + 1) + ': ')
    numbers = int(input())
    if (numbers == 0):
        zeros += 1
print('Number of numbers that are equal to zero: ' + str(zeros))
