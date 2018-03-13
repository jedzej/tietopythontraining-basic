'''
title: sum_of_three_numbers
author: arkadiusz.kasprzyk@tieto.com
date: 2018-03-05
description:
    Write a program that takes three numbers and prints their sum.
    Every number is given on a separate line.
'''

print("Takes three numbers and prints their sum.\n"
      "Every number is given on a separate line.")

a = float(input("number a = "))
b = float(input("number b = "))
c = float(input("number c = "))
s = a+b+c

print("{} + {} + {} = {}".format(a,b,c,s))


input("Press Enter to quit the program.")
