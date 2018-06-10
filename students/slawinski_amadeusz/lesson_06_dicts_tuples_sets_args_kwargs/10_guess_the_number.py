#!/usr/bin/env python3

possiblenumbers = int(input())

possible = set([str(x) for x in range(possiblenumbers)])

while True:
    readline = input()
    if readline == "HELP":
        break
    else:
        tmpset = set(readline.split())
        nextline = input()
        if nextline == "YES":
            possible &= tmpset
        elif nextline == "NO":
            possible -= tmpset
        else:
            print("Uh oh... don't know what to do")

final_list = list(possible)
final_list.sort()
final_list = [str(x) for x in final_list]
print(' '.join(final_list))
