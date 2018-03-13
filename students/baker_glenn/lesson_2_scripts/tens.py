# script to print the last digit in a given number
print("enter a number")
number = input()
if len(number) > 1:
    print("the tens digit for the number is " + str(number[len(number)-2]))
else:
    print("the tens digit for the number is 0")
