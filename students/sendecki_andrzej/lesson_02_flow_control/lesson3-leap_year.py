print("Enter the year:")
year=input()

if (int(year)%4 == 0) and (int(year)%100 != 0):
    print("LEAP")
else:
    if int(year)%400 == 0:
        print("LEAP")
    else:
        print("COMMON")
