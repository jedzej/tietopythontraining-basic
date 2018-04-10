#!/usr/bin/env python3

list = [int(x) for x in input().split()]
list_length = len(list)

greater_counter = 0

for i in range(1, list_length - 1):
    if list[i - 1] < list[i] and list[i + 1] < list[i]:
        greater_counter += 1

print(greater_counter)
