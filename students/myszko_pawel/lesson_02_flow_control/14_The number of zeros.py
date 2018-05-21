# Given N numbers: the first number in the input is N, after that N integers are given.
# Count the number of zeros among the given integers and print it.
# You need to count the number of numbers that are equal to zero, not the number of zero digits.

# Read an integer:
N = int(input())
# Print a value:
zeroes = 0
for i in range(N):
    a = int(input())
    if a == 0:
        zeroes += 1
print(zeroes)