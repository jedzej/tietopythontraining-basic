# script to sum the digits of a three digit number
print("enter a 3 digit number")
number = input()
print("the sum of the three numbers is " + str(int(number[len(number) - 3]) + int(number[len(number) - 2]) + int(number[len(number) - 1])))
