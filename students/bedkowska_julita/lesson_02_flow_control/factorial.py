number = int(input('Give the number: '))

for i in range(1, number):
    number *= i

print('{} {}'.format('Result:', number))
