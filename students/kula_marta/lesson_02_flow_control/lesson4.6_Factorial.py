#!/usr/bin/env python

number = int(input())

fact = 1
for i in range(1, number + 1):
    fact = fact * i

print(fact)
