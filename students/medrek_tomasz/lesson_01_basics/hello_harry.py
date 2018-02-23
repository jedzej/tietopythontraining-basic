#!/usr/bin/env python3

user_name = input('Enter your name:\n')
if user_name:
    hello_message = "Hello, " + user_name + "!"
    print(hello_message)
else:
    print("You didn't type anything, please try again")
