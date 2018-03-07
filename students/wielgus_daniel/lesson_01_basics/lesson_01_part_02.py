import math

#Problem1: Last digit of integer
print("We will show Last digit of integer")
print("Please provide the digit:")
a = int(input())
b = str(a)
print("The last digit is: " + b[-1])
print("THE END of Last digit of integer problem")
print("")

#Problem2: Tens digit
print("We will show Tens digit")
print("Please provide the digit:")
a = int(input())
b = str(a)
print("The Tens digit is: " + b[-2])
print("THE END of Tens digit problem")
print("")

#Problem3: Sum of digits
print("We will show sum of digit")
print("Please provide the three-digit number:")
number = int(input())
strNumber = str(number)
firstDigit = strNumber[-3]
secondDigit = strNumber[-2]
thirdDigit = strNumber[-1]
sumOfDigits = int(firstDigit) + int(secondDigit) + int(thirdDigit)
print("The sum of digits is: " + str(sumOfDigits))
print("THE END of Sum of digit problem")
print("")

#Problem4: Fractional part
print("We will show Fractional part")
print("Please provide the positive real number:")
number = float(input())
frac = str(number).split(".")[1]
print("The Fractional part of the number is: " + "0."+frac)
print("THE END of Fractional part problem")
print("")

#Problem5: First digit after decimal point
print("We will show First digit after decimal point")
print("Please provide the positive real number:")
number = float(input())
frac = str(number).split(".")[1]
fracFirstDigit = str(frac[0])
print("The Fractional part of the number is: " + fracFirstDigit)
print("THE END of First digit after decimal point problem")
print("")

#Problem6: Car route
print("We will show Car route")
print("Please provide the distance in km per day:")
kmPerDay = int(input())
print("Please provide the length of route:")	
lengthOfRoute = int(input())
days = math.ceil(lengthOfRoute / kmPerDay)
print("To cover the route (" + str(lengthOfRoute) + " km) it will take: " + str(days) + " days")
print("THE END of Car route problem")
print("")

#Problem7: Digital clock
print("We will show the digital clock")
print("Please provide the number of minutes that is past since midnight:")
passedTime = int(input())
hours = str(passedTime / 60).split(".")[0]
minutes = passedTime - int(hours)*60
if (int(hours) >= 24):
	print("It is next day :). Please provide the number of minutes which is less then 1440")
else:
	print("It is: "+str(hours)+":"+str(minutes))
print("THE END of Digital clock problem")
print("")

#Problem8: Total cost
print("We will show the Total cost problem")
print("Please provide the dollars part of price of one cupcake:")
costDollar = int(input())
print("Please provide the cents part of price of one cupcake:")
costCents = int(input())
print("Please provide quantity of cupcakes:")
quantity = int(input())
cents = quantity * costCents
centsTotalWhole = str(cents / 100).split(".")[0]
centsTotal = cents - int(centsTotalWhole)*100
dollarsTotal = quantity * costDollar + int(centsTotalWhole)
print("total cost in dollars: "+str(dollarsTotal)+" and cents: "+str(centsTotal))
print("THE END of Total cost problem")
print("")

#Problem8: Clock face -1
	#collecting data
print("We will show the Clock face -1 problem")
print("Please provide the number of hours from 0 to 12 that passed since midnight:")
hoursFromMidnight = int(input())
if (0 < hoursFromMidnight >12):
	print("there should be only 12 hours. Please try again!")
else:
	print("Please provide the number of minutes from 0 to 59 that passed since midnight:")
	minutesFromMidnight = int(input())
	if (0 < minutesFromMidnight > 59):
		print("there should be only 59 minutes. Please try again!")
	else:
		print("Please provide the number of seconds from 0 to 59 that is passed since midnight:")
		secondsFromMidnight = int(input())
		if (0 < secondsFromMidnight >59):
			print("there should be only 59 seconds. Please try again!")
		else:
				#checking the angle
			hoursAngle = 360 / 12
			minutesAngle = hoursAngle / 60
			secondsAngle = minutesAngle / 60
				#calculating the angle from midnight by multiplication of time spend from midnight and angle
			hoursAngleFromMidnight = hoursFromMidnight*hoursAngle
			minutesAngleFromMidnight = minutesFromMidnight*minutesAngle
			secondsAngleFromMidnight = secondsFromMidnight*secondsAngle
				#calculating the total angle based on above
			totalAngle = hoursAngleFromMidnight+minutesAngleFromMidnight+secondsAngleFromMidnight
				#presenting the results
			print("the angle (in degrees) of the hour hand on the clock face right now: "+str(totalAngle))
			print("THE END of Clock face -1 problem")
			print("")
