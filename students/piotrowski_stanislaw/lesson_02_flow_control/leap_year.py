# https://snakify.org/lessons/if_then_else_conditions/problems/leap_year/
# piotrsta

year = int(input('Podaj rok: '))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('LEAP')
else:
    print('COMMON')
