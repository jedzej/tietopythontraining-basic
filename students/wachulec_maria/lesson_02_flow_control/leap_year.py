year = int(input("Year: "))

if year % 400 == 0:
    print("LEAP")
elif (year % 4 == 0) and not(year % 100 == 0):
    print("LEAP")
else:
    print("COMMON")
