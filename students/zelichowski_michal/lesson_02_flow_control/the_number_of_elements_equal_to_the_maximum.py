"""A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are
equal to its largest element. """

a = int(input())
max = 0
numberOfMax = 0
while a != 0:
    if a > max:
        max = a
        numberOfMax = 1
    elif a == max:
        numberOfMax += 1
    a = int(input())
print(numberOfMax)
