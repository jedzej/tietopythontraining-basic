#Given N numbers: the first number in the input is N, after that N integers are #given. Count the number of zeros among the given integers and print it.
#
#You need to count the number of numbers that are equal to zero, not the number of #zero digits.

import sys

print("Enter the number of numbers:")
N = int(input())
if N < 1:
    print("Error: no numbers given")
    sys.exit()

zeros = 0;
print("Enter the numbers:")
for i in range(1, N+1):
    a = int(input())
    if a == 0:
        zeros = zeros + 1

print("Number of zeros:")
print(zeros)
