# Given the year number. You need to check if this year is a leap year. If
# it is, print LEAP, otherwise print COMMON.

print("Enter year")
year = int(input())

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("LEAP")
else:
    print("COMMON")
