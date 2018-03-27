# Statement
# Given the year number. You need to check if this year is a leap year.
# If it is, print LEAP, otherwise print COMMON.
# The rules in Gregorian calendar are as follows:
# a year is a leap year if its number is exactly divisible by 4 and
#  is not exactly divisible by 100
# a year is always a leap year if its number is exactly divisible by 400
# Warning. The words LEAP and COMMON should be printed all caps.


def leap_year():
    print("Enter a year:")
    a = int(input())
    if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0):
        print("LEAP")
    else:
        print("COMMON")


if __name__ == '__main__':
    leap_year()
