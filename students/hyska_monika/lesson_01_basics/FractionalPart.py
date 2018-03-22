# The program print fractional part.
from decimal import Decimal

a = Decimal(input("Please put number: "))
fr = a % 1

print("The sum of digits is:", fr)
