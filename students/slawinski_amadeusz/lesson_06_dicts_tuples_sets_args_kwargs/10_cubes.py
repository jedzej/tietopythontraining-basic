#!/usr/bin/env python3

readline = input().split()
set1no = int(readline[0])
set2no = int(readline[1])

set1 = set()
set2 = set()
for x in range(set1no):
    set1.add(int(input()))
for x in range(set2no):
    set2.add(int(input()))

inboth = sorted(set1 & set2)
onlyinset1 = sorted(set1 - set2)
onlyinset2 = sorted(set2 - set1)

print(len(inboth))
[print(x) for x in inboth]
print(len(onlyinset1))
[print(x) for x in onlyinset1]
print(len(onlyinset2))
[print(x) for x in onlyinset2]
