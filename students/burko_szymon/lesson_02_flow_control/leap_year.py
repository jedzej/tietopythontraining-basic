year = int(input("Give year: "))

if year % 4 == 0 and year % 100 != 0:
    print("LEAP")
elif year % 400 == 0:
    print("LEAP")
else:
    print("COMMON")
