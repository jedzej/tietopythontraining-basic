'''
title: last_digit_of_integer
author: arkadiusz.kasprzyk@tieto.com
date: 2018-03-05
description:
    Given an integer number, print its last digit.
'''

print("Prints last digit of a given integer.")

i = int(input("Give an integer: "))

print("The last digit is {}".format(i%10))

input("Press Enter to quit the program.")
