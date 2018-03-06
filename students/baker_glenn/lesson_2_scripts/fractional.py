# script to print the fractional part of a float
print("enter a postitve real number")
number = input()
print("the fractional part of the number is 0" + str(number[number.find("."):]))
