
n = int(input('How many numbers: '))

zero_counter = 0
for i in range(n):
    number = int(input('Integer: '))
    if number == 0:
        zero_counter += 1

print(zero_counter)
