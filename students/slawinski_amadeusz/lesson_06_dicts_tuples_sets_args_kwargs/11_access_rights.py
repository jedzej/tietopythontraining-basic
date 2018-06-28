#!/usr/bin/env python3

how_many_files = int(input())

files = {}

for i in range(how_many_files):
    name, *files[name] = input().split()

how_many_accesses = int(input())

operation_definition = {"read": "R", "write": "W", "execute": "X"}

for i in range(how_many_accesses):
    readline = input().split()
    if operation_definition[readline[0]] in files[readline[1]]:
        print("OK")
    else:
        print("Access denied")
