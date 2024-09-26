year = int(input("Enter a year to check: "))

while year > 0:
    if (year % 400 == 0):
        print("LEAP")
        break
    else:
        if (year%4 == 0) and (year%100 != 0):
            print("LEAP")
            break
        else:
            print("COMMON")
            break