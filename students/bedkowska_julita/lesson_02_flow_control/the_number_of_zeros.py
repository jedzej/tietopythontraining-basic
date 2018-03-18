numbers = int(input('Give the number of number: '))

result = 0
for i in range(numbers):
    num = int(input('Give the '+str(i + 1)+' number: '))
    if num == 0:
        result += 1

print('{} {}'.format('Number of numbers that are equal to zero:', result))
