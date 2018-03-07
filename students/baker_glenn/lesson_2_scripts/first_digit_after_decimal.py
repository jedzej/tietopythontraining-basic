# script to print the first digit of the fractional part of a float
print("enter a postitve real number")
number = input()
print("the first digit after the decimal point is " + str(number[number.find(".") + 1:number.find(".") + 2]))
