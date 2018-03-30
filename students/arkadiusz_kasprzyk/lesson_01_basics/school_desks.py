
'''
title: school_desks
author: arkadiusz.kasprzyk@tieto.com
date: 2018-03-05
description:
    A school decided to replace the desks in three classrooms.
    Each desk sits two students.
    Given the number of students in each class, print the smallest possible number of desks that can be purchased.

    The program should read three integers:
    the number of students in each of the three classes, a, b and c respectively.

    In the first test there are three groups.
    The first group has 20 students and thus needs 10 desks.
    The second group has 21 students, so they can get by with no fewer than 11 desks.
    11 desks is also enough for the third group of 22 students.
    So we need 32 desks in total.
'''

a = int(input("The number of students in class A is: "))
b = int(input("The number of students in class B is: "))
c = int(input("The number of students in class C is: "))

x = a // 2 + a%2
y = b // 2 + b%2
z = c // 2 + c%2

print("The nuber of desks for class A is {}.".format(x))
print("The nuber of desks for class B is {}.".format(y))
print("The nuber of desks for class C is {}.".format(z))

print("The total nuber of desks for all classes is {}.".format(x+y+z))

print("Thank you :)")
input("Press Enter to quit the program.")
