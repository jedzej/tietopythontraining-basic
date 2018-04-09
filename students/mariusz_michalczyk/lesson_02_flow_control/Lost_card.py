n = int(input("Enter amount of numbers: "))


entered_nrs = ""
for i in range(n-1):
    number = int(input("Enter number " + str(i) + ": "))
    entered_nrs += str(number)
for i in range(1, n+1):
    if str(i) not in entered_nrs:
        print("Lost number is: " + str(i))
