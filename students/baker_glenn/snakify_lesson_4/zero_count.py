# script to count the amount of zeros in a given set of numbers

zero_count = 0
print("enter a number")
number = input()
while number != "":
    if int(number) == 0:
        zero_count += 1
    print("enter a number")
    number = input()
print(str(zero_count))
