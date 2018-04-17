# Given the year number. You need to check if this year is
# a leap year. If it is, print LEAP,
# otherwise print COMMON.

print('Given the year number: ')
year = int(input())

if (year / 400) == int(year / 400):
    print('LEAP')
else:
    if (year / 4) == int(year / 4) and  (year / 100) != int(year / 100):
        print('LEAP')
    else:
        print('COMMON')
