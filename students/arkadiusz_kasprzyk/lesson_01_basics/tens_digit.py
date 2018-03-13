'''
title: tens_digit
author: arkadiusz.kasprzyk@tieto.com
date: 2018-03-05
description:
    Given an integer number, print its tens digit.
'''

print("Prints tens digit of a given integer.")

i = int(input("Give an integer: "))

print("The tens digit is {}".format( (i%100)//10 ))


input("Press Enter to quit the program.")