y = int(input('year: '))

if y % 4 == 0 and  y % 100 != 0:
    print('leap')
elif y % 400 == 0:
    print('leap')
else:
    print('common')
