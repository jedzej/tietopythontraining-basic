#!/usr/bin/env python

n = input("set minutes: ")
h = n/60
m = n - h*60

print("%02d:%02d") %(h, m)