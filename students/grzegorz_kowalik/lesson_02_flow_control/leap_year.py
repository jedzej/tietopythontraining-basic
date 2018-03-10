year = int(input())

if year % 400 == 0:
    print("LEAP")
elif year % 100 == 0:
    print("COMMON")
elif year % 4 == 0:
    print("LEAP")
else:
    print("COMMON")
