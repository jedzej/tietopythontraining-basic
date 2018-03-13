yyyy = int(input())

if (yyyy % 400 == 0 ) or (yyyy % 100 != 0) and (yyyy % 4 == 0):
    print("LEAP")
else:
    print("COMMON")
