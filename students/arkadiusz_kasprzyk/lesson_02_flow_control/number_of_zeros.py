"""
description:
    Given N numbers: the first number in the input is N, after that N integers are given.
    Count the number of zeros among the given integers and print it.
    You need to count the number of numbers that are equal to zero, not the number of zero digits.
"""

print("""
    Given N numbers: the first number in the input is N, after that N integers are given.
    Counts the number of zeros among the given integers and prints it.
""")

N = int(input("Give N (number of integers to be given) : "))

zeros_counter = 0

for k in range(N):
    nr = int(input("give {}-th number: ".format(k+1)))
    zeros_counter += nr == 0

print("There were {} zeros.".format(zeros_counter))
