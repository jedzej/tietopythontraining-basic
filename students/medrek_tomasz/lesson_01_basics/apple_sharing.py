#!/usr/bin/env python3

given_numbers = []

for i in range(2):
    try:
        given_numbers.append(int(input("Please enter a number:\n")))
    except ValueError:
        print('That was not a valid number, please try again')
        exit()

number_of_students = given_numbers[0]
number_of_apples = given_numbers[1]

apples_in_basket = number_of_apples % number_of_students
apples_per_student = number_of_apples // number_of_students

print(apples_per_student)
print(apples_in_basket)
