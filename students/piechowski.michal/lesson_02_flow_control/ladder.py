#!/usr/bin/env python3

number_of_steps = int(input())
ladder = ""

for i in range(1, number_of_steps + 1):
    ladder += str(i)
    print(ladder)
