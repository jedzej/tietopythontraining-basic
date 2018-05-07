#!/usr/bin/env python3

readline = input()
ages = [int(x) for x in readline.split()]

adults = [x for x in ages if x >= 18]
kids = [x for x in ages if x < 18]

average = 0
if adults:
    for i in adults:
        average = average + i
    average = average / len(adults)

print("Average adult age: " + str(average))
print("Kids: " + str(len(kids)))
