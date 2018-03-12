year = int(input('Enter year\n'))
if ((not(year % 4) and (year % 100)) or not(year % 400)):
    print('LEAP')
else:
    print('COMMON')
