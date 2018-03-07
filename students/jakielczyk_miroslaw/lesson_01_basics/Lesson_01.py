# Sum of three numbers
a = int(input("Enter number 1"))
b = int(input("Enter number 2"))
c = int(input("Enter number 3"))
print ("Sum of these three numbers ",(a+b+c))

# Area of right-angled triangle
print ("Enter length of the base of a right-angled triangle")
a = float(input())
print ("Enter height of the right-angled triangle")
h = float(input())
s=a*h/2
print ("Surface of operacje_matematyczne.py ",s)

# Hello, Harry!
a = input("Enter the name to be displayed ")
a = "Hello, "+a+"!"
print (a)

# Apple sharing
n = int(input())
k = int(input())
x = k//n
y = k%n
print (x)
print (y)

# Previous and next
n = int(input())
print (n+1)
print (n-1)

# School desks
a = int(input())
b = int(input())
c = int(input())
num = a//2+b//2+c//2 + a%2+b%2+c%2
print (num)

# Last digit of integer
x=input()
print (x[-1])

# Tens digit
x=int(input())
print((x%100)//10)

# Sum of digits
x=int(input())
x=str(x)
sumary = 0
for digit in x:
    sumary+=int(digit)
print (sumary)

# Fractional part
x=float(input())
print (x-int(x))

# First digit after decimal point
x=float(input())
x=x-int(x)
x=str(x)[2]
print (x)

# Car route
n=int(input())
m=int(input())
if m%n == 0:
    print (m//n)
else:
    print(1+m//n)

# Digital clock
n=int(input())
hour = n//60
minutes=n%60
print (hour, minutes)

# Total cost
a=int(input())
b=int(input())
n=int(input())
total_dolars = ((a*100+b)*n)//100
total_cents = ((a*100+b)*n)%100
print (total_dolars, total_cents)

# Clock face - 1
h=float(input())
m=float(input())
s=float(input())
angle = 360*(h*60*60 + m*60 + s)/(12*3600)
print (angle)

# Clock face - 2
a=float(input())
minute=(12*60*(a/360))%60
angle = minute*360/60
print (angle)




