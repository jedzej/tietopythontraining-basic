"""
description:
    Given the year number.
    You need to check if this year is a leap year.
    If it is, print LEAP, otherwise print COMMON.

    The rules in Gregorian calendar are as follows:
    * a year is a leap year if its number is exactly divisible by 4 and is not exactly divisible by 100
    * a year is always a leap year if its number is exactly divisible by 400
"""

print("Determines if given year is leap or common.")

year = int(input("give a year: "))

div_by_4 = year % 4 == 0
div_by_100 = year % 100 == 0
div_by_400 = year % 400 == 0

if (div_by_4 and not div_by_100) or div_by_400:
    print("LEAP")
else:
    print("COMMON")
