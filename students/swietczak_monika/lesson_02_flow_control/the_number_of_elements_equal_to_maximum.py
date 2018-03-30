the_highest = 0
count = 0

number = int(input("Enter a number: "))
while number != 0:
    if number > the_highest:
        the_highest = number
        count = 1
    elif number == the_highest:
        count += 1
    number = int(input("Enter another number: "))
# Print a value:
print(count)
