# lesson_01_basics
# First digit after decimal point
#
# Statement
# Given a positive real number, print its first digit to the right of the decimal point.

print("Enter a positive real number")
n = float(input())

res = int(n * 10) % 10

print("First digit to the right of '.' is: " + str(res) + ".")

