# Lesson 1 (Input, print and numbers)

print('Problem 1: Sum of three numbers')
print('Set first number:')
a = int(input())
print('Set second number:')
b = int(input())
print('Set third number:')
c = int(input())
print(a + b + c)

print('\n\rProblem 2: Area of right-angled triangle')
print('Set length of the base of a right-angled triangle')
b = int(input())
print('Set length of the height of a right-angled triangle')
h = int(input())
print('The area of right-angled triangle is equal: ' + str((1/2)*b*h))

print('\n\rProblem 3: Hello, Harry!')
print('Set user name: ')
name = input()
print('Hello, ' + str(name) + '!')

print('\n\rProblem 4: Apple sharing')
print('Set number of students:')
N = int(input())
print('Set number of apples:')
K = int(input())
print('Each student get ' + str(K // N) + ' apples')
print('In basket remains ' + str(K % N) + ' apples')

print('\n\rProblem 5: Previous and next')
print('Set an integer:')
a = int(input())
print('The next number for the number ' + str(a) + ' is ' + str(a + 1) + '.')
print('The previous number for the number ' + str(a) + ' is ' + str(a - 1) + '.')

print('\n\rProblem 6: School desks')
def compute_desks( nr ):
    return ((nr + (nr % 2)))>>1;
myClass =['a','b','c']
a = 0

for x in range(0, 3):
    print('Set number of students in class ' + myClass[x] + ' :')
    a += compute_desks( int(input()))
print('So we need ' + str(a) + ' desks in total.')


# Lesson 2 (Integer and float numbers)

print('\n\rProblem 1: Last digit of integer')
print('Set number of integer:')
a = int(input())
print('Last digit of integer is: ' + str(a % 10))

print('\n\rProblem 2: Tens digit.')
print('Set an integer:')
a = int(input())
print('Tens digit from integer is equal ' + str( (a%100)//10 ) )

print('\n\rProblem 3: Sum of digits.')
print('Set an integer:')
a = int(input())
first = a % 10
second = (a%100)//10
third = (a%1000)//100
print('Tens digit from integer is equal ' + str( first + second + third ) + '.')

print('\n\rProblem 4: Fractional part.')
print('Set an positive real number:')
a = float(input())
print('Fractional part from positive real number is equal '+ str(a%1))

print('\n\rProblem 5: First digit after decimal point')
from math import floor
print('Set an positive real number:')
a = float(input())
print('Fractional part from positive real number is equal '+ str(floor((a%1)*10)) + '.')

print('\n\rProblem 6: Car route')
from math import ceil
print('Set car cover distance per day[km]:')
N = int(input())
print('Set total length of route[km]:')
M = int(input())
print('Number of days per route: ' + str(ceil(M/N)))

print('\n\rProblem 7: Digital clock')
print('Set the number of minutes that are passed since midnight')
N = int(input())
hours = int(N // 60)
minutes = N - (hours * 60)
print('On the digital clock is:')
print(str(hours) + ' ' + str(minutes))

print('\n\rProblem 8: Total cost')
print('Set dollar part cost per cupcake:')
A = int(input())
print('Set cent part cost per cupcake:')
B = int(input())
print('Set nr of cupcake:')
N = int(input())
total_cents = (A * 100 + B ) * N
dollars = total_cents // 100
cents = total_cents - ( dollars * 100 )
print('Total cost: ' + str(dollars) + ' ' + str(cents))

print('\n\rProblem 9: Clock face - 1')
print('Set hours:')
H = int(input())
print('Set minutes:')
M = int(input())
print('Set seconds:')
S = int(input())
total_minutes = S/60 + M + H*60
angle = total_minutes * 0.5
print('The angle is equal %.3f' % angle)
