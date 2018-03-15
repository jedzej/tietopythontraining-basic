import math
# Read an integer:
# a = int(input())
# Print a value:
# print(a)

dollars = int(input())
cents = int(input())
cupCakes = int(input())

price = float(dollars) + float(cents*0.01)
floatPriceTotal = price*cupCakes

totalDollars = int(floatPriceTotal)
totalCents = int(round(floatPriceTotal%1*100))

print((str(totalDollars)+' '+str(totalCents)))