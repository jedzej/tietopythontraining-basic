#!/usr/bin/env python3
import math
# ===================================
# Lesson 1. Input, print and numbers
# ===================================

# Input, print and numbers

a = int(input())

b = int(input())

c = int(input())

print(a + b + c)

# ==========================

# Area of right-angled triangle

b = int(input())

h = int(input())

print((b*h)/2)

# ==========================

# Hello, Harry!

a = input()


print("Hello, "+a+"!")

# =====================================

# Apple sharing

n = int(input())

k = int(input())


print(k // n)

print(k % n)

# ==========================

# Previous and next

a = int(input())

print("The next number for the number %s is %s."% (a, (a+1)))

print("The previous number for the number %s is %s."% (a, (a-1)))


# =============================================

# School desks

a = int(input())

b = int(input())

c = int(input())


d= a//2+b//2+c//2 + a%2+b%2+c%2

print(d)


# ===========================
# Lesson 2. Integer and float numbers
# ===========================

# Last digit of integer


a = int(input())

print(a%10)

# =============================

# Tens digit


a = int(input())


print((a%100)//10)

# ============================

# Sum of digits


a = int(input())

b=a%10 + (a//10)%10  + (a//100)%10 


print(b)

# =================================

# Fractional part


a = float(input())


print(a-(a//1))

# =================================

# First digit after decimal point


a = float(input())


b = ((a*10)//1)%10

print(b)


# ==========================

# Car route


N = int(input())

M = int(input())

m = math.ceil(M/N)

print(str(m))


# ======================

# Digital clock

a = int(input())

h=a//60

m=a%60

print('%s %s' % (h, m))


# ===========================

# Total cost

dollar = int(input())

cent = int(input())

amount = int(input())

sum1=((dollar*100)+cent)

sum2=(sum1*amount)

dollar2=(sum2//100)

cent2=(sum2%100)

print("%i %i" % (dollar2,cent2))


# =============================

# Clock face - 1

h = int(input())

m = int(input())

s = int(input())


hr=360*(h/12)
mi=(360/12)*(m/60)

se=(360/12/60)*(s/60)

a=hr+mi+se
print(a)

# ===========================




