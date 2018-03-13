'''
title: prevous_and_next
author: arkadiusz.kasprzyk@tieto.com
date: 2018-03-05
description:
    Write a program that reads an integer number and prints its previous and next numbers.
    There shouldn't be a space before the period.
'''

print('''Reads an integer number and prints its previous and next numbers.
'''
)

n = int(input("Give an integer: "))

print("The next number to {} is {}".format(n,n+1))
print("The previous number to {} is {}".format(n,n-1))


input("Press Enter to quit the program.")