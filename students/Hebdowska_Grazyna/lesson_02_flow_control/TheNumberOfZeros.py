number = int(input('N: '))
number_of_zeros = 0
for i in range(0, number):
    new_number = int(input('n: '))
    if new_number == 0:
        number_of_zeros += 1

print(number_of_zeros)
