# lesson_01_basics
# Fractional part
#
# Statement
# Given a positive real number, print its fractional part. 

print("Enter a positive real number")
n = float(input())

res = n - int(n)

print("Fractional part is: " + str(res) + ".")

