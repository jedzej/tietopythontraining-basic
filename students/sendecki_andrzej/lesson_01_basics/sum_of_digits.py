# lesson_01_basics
# Sum of digits
#
# Statement
# Given a three-digit number. Find the sum of its digits.

print("Enter 3 digit number")
n = int(input())
n = abs(n)

d1 = n // 100 % 10
d2 = n // 10 % 10
d3 = n % 10

sum = d1 + d2 + d3

print("Sum of digits is: " + str(sum) + ".")

