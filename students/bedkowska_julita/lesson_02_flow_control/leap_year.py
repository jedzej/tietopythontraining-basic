year = int(input('Input year: '))

result = 'COMMON'

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    result = 'LEAP'

print('{} {}'.format('The year is:', result))
