#!/usr/bin/env python

n = int(input())
fact = 1
fact_sum = 0

for i in range(1, n + 1):
    fact *= i
    fact_sum += fact

print(fact_sum)
