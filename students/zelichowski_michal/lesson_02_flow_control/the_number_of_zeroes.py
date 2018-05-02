"""Given N numbers: the first number in the input is N, after that N
integers are given. Count the number of zeros among the given integers
and print it.

You need to count the number of numbers that are equal to zero,
not the number of zero digits. """

# Read an integer:
a = int(input())
zeroes = 0
for x in range(1, a+1):
    b = int(input())
    if b == 0:
        zeroes += 1

# Print a value:
print(zeroes)
