#1 Sum of three numbers

a = int(input())
b = int(input())
c = int(input())
print(a+b+c)

#2 Area of right-angled triangle
a = int(input())
b = int(input())
print(0.5*a*b)

#3 Hello, Harry!

a = input()
print("Hello, "+ a + "!")

#4 Apple sharing
a = int(input())
b = int(input())
print(b//a)
print(b%a)

#5 Previous and next
a = int(input())
print('The next number for the number ' + str(a)  + " is " + str(a+1) + ".")
print('The previous number for the number ' + str(a)  + " is " + str(a-1) + ".")

#6 School desks
a = int(input())
b = int(input())
c = int(input())

l = [a,b,c]
sum = 0
for x in l:
    if x%2 != 0:
        z = ((x+1)/2)
        sum += z
    else:
        z = (x/2)
        sum += z
print(sum)

#---------------------------
#PART 2
#---------------------------

#1 Last digit of integer
a = int(input())
print(a%10)

#2 Tens digit
a = str(input())
print(a[-2])

#3 Sum of digits
a = str(input())
changeToString = str(a)
sum = 0
for eachNumber in changeToString:
    sum += int(eachNumber)
print(sum)

#4 Fractional part
import math
a = float(input())
frac, whole = math.modf(a)
print(frac)

#5 First digit after decimal point
import math
a = float(input())
fraction = math.modf(a)
fractionFirstElement = str(fraction[0])
print(fractionFirstElement[2])

#6 Car route
import math
distanceCarCanTravel = int(input())
distanceToTravel = int(input())
print(math.ceil(distanceToTravel/distanceCarCanTravel))

#7 Digital clock
import datetime
minutesPassedSinceMidnight =int(input())
print(datetime.timedelta(minutes=minutesPassedSinceMidnight))

#8 Total cost
dollars = int(input())
cents = int(input())
howManyCupcakes = int(input())
price = dollars + (cents/100)
howManyShouldIpay = price*howManyCupcakes

dollarsInTotalToPay, centsInTotalToPay = divmod(howManyShouldIpay, 1)
print(int(dollarsInTotalToPay), centsInTotalToPay*100)

#9 Clock face - 1
while True:
    hours = int(input("Give me a hour between 0-12: "))
    if hours > 12:
        print("Number must be smaller than 12")
        continue
    elif hours < 0:
        print("Number must be bigger than 0")
        continue
    else:
        minutes = int(input("Give me a minutes between 0-60: "))
        if minutes > 60:
            print("Number must be smaller than 60")
            continue
        elif minutes < 0:
            print("Number must be bigger than 0")
            continue
        else:
            seconds = int(input("Give me a seconds between 0-60"))
            if seconds > 60:
                print("Number must be smaller than 60")
                continue
            elif seconds < 0:
                print("Number must be bigger than 0")
                continue
            else:
                break
print(hours, minutes, seconds)

print(hours*30 + minutes*30/60 + seconds*30/3600)
