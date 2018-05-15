#!/usr/bin/env python

list = []
x = int(input("enter the number of variables to verify: "))


for i in range(x):
    e = int(input())
    list.append(e)

print list.count(0)
