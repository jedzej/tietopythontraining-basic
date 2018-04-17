#!/usr/bin/env python3

number_of_steps = int(input())

if number_of_steps > 9:
    print("Maximum 9 is allowed")
    quit()

ladder = ""

for i in range(1, number_of_steps + 1):
    ladder += str(i)
    print(ladder)
