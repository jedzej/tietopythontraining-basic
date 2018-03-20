the_highest = 0
the_second = 0

number = int(input("Enter a number: "))
while number != 0:
    if number > the_highest:
        the_second = the_highest
        the_highest = number
    elif number > the_second:
        the_second = number
    number = int(input("Enter another number: "))
# Print a value:
print(the_second)
