print("Leap year\n")

a = int(input("Give a year number: "))

if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("LEAP")
else:
    print("COMMON")
