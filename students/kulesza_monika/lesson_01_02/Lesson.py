def sum_of_three_numbers():
    a = int(input())
    b = int(input())
    c = int(input())

    print(a + b + c)
#####################################################

def area_of_right_angled_triangle():
    b = int(input())
    h = int(input())

    print (0.5 * b * h)
#####################################################

def hello_harry():
    a = input()

    print("Hello, " + a + "!")
#####################################################

def apple_sharing():
    n = int(input())
    k = int(input())

    print(k // n)
    print(k % n)
#####################################################

def previous_and_next():
    a = int(input())

    print("The next number for " + str(a) + " is " + str(a + 1) + ".")
    print("The previous number for " + str(a) + " is " + str(a - 1) + ".")
#####################################################

def school_desks():
    a = int(input())
    b = int(input())
    c = int(input())

    desks = (a % 2 + a // 2) + (b % 2 + b // 2) + (c % 2 + c // 2)
    print (desks)
#####################################################

def last_digit_of_integer():
    a = int(input())

    lastdigit = int(repr(a)[-1])
    print(lastdigit)
#####################################################

def tens_digit():
    a = int(input())
    tens = int(repr(a)[-2])
    print(tens)
#####################################################

def sum_of_digits():
    a = str(input())

    list1 = []
    for each_number in a:
        list1.append(int(each_number))
    print(sum(list1))
#####################################################

def fractional_part():
    a = float(input())

    dec = str(a - int(a))[1:]
    print (dec)

OORRRRRR
a = float(input())
from decimal import Decimal
Decimal(a) % 1
#####################################################

def first_digit_after_decimal_point():
    a = float(input())

    dec = str(a - int(a))[2:3]
    print (dec)
#####################################################

import math
def car_route():
#N - kilometers per day; M - distance
    N = int(input())
    M = int(input())

    print(math.ceil(M / N))
#####################################################

def digital_clock:
    a = int(input())

    clock = a // 60
    clock_min = a % 60
    print (clock, clock_min)
#####################################################

def total_cost():
    a = int(input())
    b = int(input())
    c = int(input())

    total = c * a + (c * b * 0.01)
    dec = str(total - int(total))[2:4]

    print (round(total), dec)
#####################################################

def clock_face_1():
    h = int(input())
    min = int(input())
    sec = int(input())

    clock = 0.5 * (h * 60 + min + sec / 60)
    print (clock)
#####################################################

def clock_face_2():
    a = int(input())

    clock = (a * 12) % 360
    print (clock)











