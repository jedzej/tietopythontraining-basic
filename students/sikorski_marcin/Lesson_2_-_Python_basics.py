#Lesson_3
#Leap Year
year = int(input("Enter year to check: "))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('LEAP')
else:
    print('COMMON')

#Chocolate bar
first_value_of_portion_ortion = int(input("Enter first value: "))
second_value_of_portion = int(input("Enter second value: "))
number_of_squares = int(input("Enter number of squares: "))

if (number_of_squares %first_value_of_portion_ortion == 0 and number_of_squares /first_value_of_portion_ortion < second_value_of_portion) or (number_of_squares %second_value_of_portion== 0 and number_of_squares /second_value_of_portion < first_value_of_portion_ortion):
    print("YES - we can divide choclate!")
else:
    print("NO - we can't divide chocolate")

#Knight move
first_column = int(input("Enter first column: "))
first_row = int(input("Enter first row: "))
second_column = int(input("Enter second column: "))
second_row = int(input("Enter second row: "))

row = abs(first_row-second_row)
column = abs(first_column -second_column)

if row == 2 and column == 1 or row == 2 and column == 1:
    print("YES - we can move there!")
else:
    print("NO - we can't move there!")

#Queen move
first_column = int(input("Enter first column: "))
first_row = int(input("Enter first row: "))
second_column = int(input("Enter second column: "))
second_row = int(input("Enter second row: "))

row = abs(first_row-second_row)
column = abs(first_column -second_column)


if row == column or first_row == second_row or first_column == second_column:
    print("YES - we can move the queen there!")
else:
    print("NO - we can't move queen there")

#Bishop Moves
first_column = int(input("Enter first column: "))
first_row = int(input("Enter first row: "))
second_column = int(input("Enter second column: "))
second_row = int(input("Enter second row: "))

row = abs(first_row -second_row)
column = abs(first_column-second_column)

if row == column:
    print("YES - we can move bishop there!")
else:
    print("NO - we can't move bishop there!")

#Lesson 4
#Lost cards
number_of_cards = int(input("Enter number of cards: "))
sum_of_number_of_cards = (((1 + number_of_cards)/2) * number_of_cards)

sum = 0
while number_of_cards != 1:
    number = int(input("Type NOT MISSING numbers: "))
    number_of_cards -= 1
    sum += number

print("Number of lost cards: " +str(sum_of_number_of_cards-sum))

#Ladder
number_of_steps = int(input("Enter number of steps: "))

for x in range(1, number_of_steps + 1):
    for y in range(1, x + 1):
        print(y, sep='', end='')
    print()

#Adding factorials
number_to_check = int(input("Give me a number to do facorial" ))

which_factoral = 1
sum=0

if number_to_check != 0:
    for i in range (1, number_to_check+1):
        which_factoral *= i
        sum += which_factoral
    print(sum)
else:
    print(1)

#The number of zeroes
number_of_zeroes = 0

for i in range(int(input("How many numbers you want to type? "))):
    if int(input("Type the number "+ str(i+1) + "  ")) == 0:
        number_of_zeroes += 1
print("You have " + str(number_of_zeroes) + " zeroes.")

#Factorial

factorial = int(input("Type the number: "))
starter = 1

for i in range(2, factorial+1):
    starter *= i
print(starter)

#Lesson 6
#The number of elements equal to the maximum

maximum = 0
how_many_maximum_numbers = 0
counter = 1

print("Type the numbers. Stop with 0.")

while counter != 0:
    counter = int(input())
    if counter > maximum:
        maximum, how_many_maximum_numbers = counter, 1
    elif counter == maximum:
        how_many_maximum_numbers += 1
print("Maxium number appears: " + str(how_many_maximum_numbers))