print('What is the year you want to check? ')
year = int(input())
if year % 4 == 0 and year % 100 != 0:
    if year % 400 == 0:
        print('LEAP')
    else:
        print('COMMON')
