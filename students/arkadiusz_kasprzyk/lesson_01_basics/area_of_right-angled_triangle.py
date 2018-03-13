'''
title: area_of_right-angled_triangle
author: arkadiusz.kasprzyk@tieto.com
date: 2018-03-05
description:
    Write a program that reads the length of the base and the height of a right-angled triangle and prints the area.
    Every number is given on a separate line.
'''

print("Reads the length of the base and the height of a right-angled triangle and prints the area.\n"
      "Every number is given on a separate line.")

b = float(input("give base length: "))
h = float(input("give height: "))

a = b*h/2

print("The area of the triangle is {}".format(a))


input("Press Enter to quit the program.")

