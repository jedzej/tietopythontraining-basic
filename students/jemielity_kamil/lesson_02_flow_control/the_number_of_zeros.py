n = int(input('How many numbers: '))

zero_couner = 0
for i in range(n):
    number = int(input('Integer: '))
    if number == 0:
        zero_couner += 1

print(zero_couner)
