# Lesson 1.Input, print and numbers
# Sum of three numbers
first = int(input())
second = int(input())
third = int(input())
sum = first + second + third
print(sum)

# Area of right-angled triangle
base = int(input())
height = int(input())
area = (base * height) / 2
print(area)

# Hello, Harry!
print('Hello, ' + str(input()) + '!')

# Apple sharing
students = int(input())
apples = int(input())
print(apples // students)
print(apples % students)

# Previous and next
number = int(input())
print('The next number for the number ' + str(number) + ' is ' + str(number + 1) + '.')
print('The previous number for the number ' + str(number) + ' is ' + str(number - 1) + '.')

# School desks
class1 = int(input())
class2 = int(input())
class3 = int(input())
desks = class1 // 2 + class2 // 2 + class3 // 2 + class1 % 2 + class2 % 2 + class3 % 2
print(desks)

# Lesson 2.Integer and float numbers
# Last digit of integer
intnum = int(input())
print(intnum%10)

# Tens digit
tensdig = int(input())
print((tensdig % 100) // 10)

# Sum of digits
sum3dig = int(input())
print(((sum3dig % 1000) // 100) + ((sum3dig % 100) // 10) + (sum3dig % 10))

# Fractional part
fract = float(input())
print(fract - int(fract))

# First digit after decimal point
rand = float(input())
firstdig = ((rand*10)//1)%10
print(int(firstdig))

# Car route


# Digital clock


# Total cost


# Clock face - 1

