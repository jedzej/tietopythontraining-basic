'''
title: hello_harry
author: arkadiusz.kasprzyk@tieto.com
date: 2018-03-05
description:
    Write a program that greets the user by printing the word "Hello", a comma,
    the name of the user and an exclamation mark after it. See the examples below.
    Warning. Your program's output should strictly match the desired one, character by character.
    There shouldn't be any space between the name and the exclamation mark.
    You can use + operator to concatenate two strings. See the lesson for details.
'''

nam = input("What's your name: ")
print("Hello, {}!".format(nam))
input("Press Enter to quit.")