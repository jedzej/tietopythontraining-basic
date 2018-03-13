'''
title: tens_digit
author: arkadiusz.kasprzyk@tieto.com
date: 2018-03-05
description:
    Given a three-digit number. Find the sum of its digits.
'''

print("Prints sum of digits of a 3-digit integer.")

i = int(input("Give an integer: "))

s = i//100 + (i%100)//10 + i%10


print("The tens digit is {}".format(s))

input("Press Enter to quit the program.")