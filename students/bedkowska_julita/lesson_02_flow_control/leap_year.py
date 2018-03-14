year = int(input())

result = 'COMMON'

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    result = 'LEAP'

print('The year is: '+result)
