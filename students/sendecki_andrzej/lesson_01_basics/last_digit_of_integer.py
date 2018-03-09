# lesson_01_basics
# Last digit of integer
#
# Statement
# Given an integer number, print its last digit. 

import math

print("Enter the number")
n = int(input())
res = abs(n) % 10

print("The last digit is: " + str(res))
