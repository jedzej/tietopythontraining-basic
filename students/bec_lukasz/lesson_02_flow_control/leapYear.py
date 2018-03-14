# Read an integer:
# a = int(input())
# Print a value:
# print(a)

year = int(input())

if year % 4 == 0 and year % 100 != 0:
    print('LEAP')
elif year % 400 == 0:
    print('LEAP')
else:
    print('COMMON')
	