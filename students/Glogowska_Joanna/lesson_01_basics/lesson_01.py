import math

# Lesson 1.Input, print and numbers
# Sum of three numbers
print('Input three numbers in different rows')
first = int(input())
second = int(input())
third = int(input())
sum = first + second + third
print(sum)

# Area of right-angled triangle
print('Input the length of the triangle')
base = int(input())
print('Input the height of the triangle')
height = int(input())
area = (base * height) / 2
print(area)

# Hello, Harry!
print('What is your name?')
print('Hello, ' + str(input()) + '!')

# Apple sharing
print('Input number of students')
students = int(input())
print('Input number of apples')
apples = int(input())
print('Each student will get ' + str(apples // students) + ' apples')
print(str(apples % students) + ' apples will remain in the basket')

# Previous and next
number = int(input())
print('The next number for the number ' + str(number) + ' is ' +
      str(number + 1) + '.')
print('The previous number for the number ' + str(number) + ' is ' +
      str(number - 1) + '.')

# School desks
print('There are 3 classes - how many students is in each of them?\n"'
      'Input your answers in separate rows')
class1 = int(input())
class2 = int(input())
class3 = int(input())
desks = (
    class1 // 2 + class2 // 2 + class3 // 2 +
    class1 % 2 + class2 % 2 + class3 % 2
)
print(str(desks) + ' needs to be purchased')

# Lesson 2.Integer and float numbers
# Last digit of integer
intnum = int(input())
print(intnum % 10)

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
firstdig = ((rand * 10) // 1) % 10
print(int(firstdig))

# Car route
print('What distance in km the car covers per day?')
kmperday = int(input())
print('What is the length of the route?')
routelength = int(input())
print(math.ceil(routelength / kmperday))

# Digital clock
print('Number of minutes that passed since midnight')
minsmidn = int(input())
print(str(minsmidn // 60) + ':' + str(minsmidn % 60))

# Total cost
dollars = int(input())
cents = int(input())
numcup = int(input())
print(dollars * numcup + (cents * numcup) // 100, (cents * numcup) % 100)

# Clock face - 1
print('How many hours have passed since minight?')
hours = int(input())
print('How many minutes have passed since minight?')
mins = int(input())
print('How many seconds have passed since minight?')
secs = int(input())
anghr = 360 / 12
angmin = anghr * 1 / 60
angsec = angmin / 60
angle = (anghr * hours) + (angmin * mins) + (angsec * secs)
print(angle)
