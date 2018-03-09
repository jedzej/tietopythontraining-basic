# lesson_01_basics
# Tens digit
#
# Statement
# Given an integer. Print its tens digit. 

import math

print("Enter the number")
n = int(input())
res = abs(n) // 10 % 10

print("The tens digit is: " + str(res))
