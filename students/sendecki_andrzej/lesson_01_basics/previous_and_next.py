# lesson_01_basics
# Previous and next
#
# Statement
# Write a program that reads an integer number and prints its previous and next numbers.
# See the examples below for the exact format your answers should take.
# There shouldn't be a space before the period.

print("Enter the number")

n = int(input())
n_next = n + 1
n_prev = n - 1

print("The next number for the number " + str(n) + " is " + str(n_next) + ".")
print("The previous number for the number " + str(n) + " is " + str(n_prev) + ".")

