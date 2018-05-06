#!/usr/bin/env python3

lines = int(input())

uniquewords = set()

for i in range(lines):
    uniquewords.update(input().split())

print(len(uniquewords))
