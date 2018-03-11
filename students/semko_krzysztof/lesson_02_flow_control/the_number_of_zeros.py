"""
Given N numbers: the first number in the input is N, after that N integers are given.
Count the number of zeros among the given integers and print it.

You need to count the number of numbers that are equal to zero, not the number of zero digits.
"""

print("Please input number if integers that will be inputted:")
number = int(input())
zero_count = 0;
print("Input " + str(number) + " integers:")
for i in range(number):
    i = int(input())
    if i == 0:
        zero_count += 1
print("Total number of zero integers is: " + str(zero_count))
