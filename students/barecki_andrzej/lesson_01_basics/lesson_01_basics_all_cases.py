# Lesson 1 (Input, print and numbers) and # Lesson 2 (Integer and float numbers)3
import os
import math

print('Problem 1: Sum of three numbers')
print('Set first number:')
a = int(input())
print('Set second number:')
b = int(input())
print('Set third number:')
c = int(input())
result = a + b + c
print(str(result) + os.linesep)

print('Problem 2: Area of right-angled triangle')
print('Set length of the base of a right-angled triangle')
b = int(input())
print('Set length of the height of a right-angled triangle')
h = int(input())
print('The area of right-angled triangle is equal: ' + str((1 / 2) * b * h) + os.linesep)

print('Problem 3: Hello, Harry!')
print('Set user name: ')
name = input()
print('Hello, ' + str(name) + '!' + os.linesep)

print('Problem 4: Apple sharing')
print('Set number of students:')
N = int(input())
print('Set number of apples:')
K = int(input())
print('Each student get ' + str(K // N) + ' apples')
print('In basket remains ' + str(K % N) + ' apples' + os.linesep)

print('Problem 5: Previous and next')
print('Set an integer:')
a = int(input())
print('The next number for the number ' + str(a) + ' is ' + str(a + 1) + '.')
print('The previous number for the number ' + str(a) + ' is ' + str(a - 1) + '.' + os.linesep)

print('Problem 6: School desks')


def compute_desks(nr):
    return (nr + (nr % 2)) >> 1


a = 0
i = 0
while True:
    a += compute_desks(int(input()))
    i += 1
    if i == 3:
        break
print(str(a) + os.linesep)

# Lesson 2 (Integer and float numbers)3
print('Problem 1: Last digit of integer')
print('Set number of integer:')
a = int(input())
print('Last digit of integer is: ' + str(a % 10) + os.linesep)

print('Problem 2: Tens digit.')
print('Set an integer:')
a = int(input())
print('Tens digit from integer is equal ' + str((a % 100) // 10) + os.linesep)

print('Problem 3: Sum of digits.')
print('Set an integer:')
a = int(input())
first_digit = a % 10
second_digit = (a % 100) // 10
third_digit = (a % 1000) // 100
print('Tens digit from integer is equal ' + str(first_digit + second_digit + third_digit) + '.' + os.linesep)

print('Problem 4: Fractional part.')
print('Set an positive real number:')
a = float(input())
print('Fractional part from positive real number is equal ' + str(a % 1) + os.linesep)

print('Problem 5: First digit after decimal point')
print('Set an positive real number:')
a = float(input())
print('Fractional part from positive real number is equal ' + str(int(math.floor((a % 1) * 10))) + '.' + os.linesep)

print('Problem 6: Car route')
print('Set car cover distance per day[km]:')
N = int(input())
print('Set total length of route[km]:')
M = int(input())
print('Number of days per route: ' + str(math.ceil(M / N)) + os.linesep)

print('Problem 7: Digital clock')
print('Set the number of minutes that are passed since midnight')
N = int(input())
hours = int(N // 60)
minutes = N - (hours * 60)
print('On the digital clock is:')
print(str(hours) + ' ' + str(minutes) + os.linesep)

print('Problem 8: Total cost')
print('Set dollar part cost per cupcake:')
dollar_part_cost = int(input())
print('Set cent part cost per cupcake:')
cent_part_cost = int(input())
print('Set nr of cupcake:')
cupcake_nr = int(input())
total_cents = (dollar_part_cost * 100 + cent_part_cost) * cupcake_nr
dollars = total_cents // 100
cents = total_cents - (dollars * 100)
print('Total cost: ' + str(dollars) + ' ' + str(cents) + os.linesep)

print('Problem 9: Clock face - 1')
print('Set hours:')
H = int(input())
print('Set minutes:')
M = int(input())
print('Set seconds:')
S = int(input())
total_minutes = S / 60 + M + H * 60
angle = total_minutes * 0.5
print('The angle is equal %.3f' % angle)
