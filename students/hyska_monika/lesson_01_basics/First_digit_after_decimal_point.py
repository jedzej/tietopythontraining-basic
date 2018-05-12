# The program  print first digit to the right of the decimal point.
from decimal import Decimal

a = Decimal(input("Please put number: "))
fr = a % 1
z = int(fr * 10)

print("First digit after decimal point is:", z)
