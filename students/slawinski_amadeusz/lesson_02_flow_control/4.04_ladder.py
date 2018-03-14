# print n step ladder with integers from 1 to k on k step

steps = int(input())

if steps > 0 and steps < 10:
    for k in range(1, steps + 1):
        print(*range(1, k + 1), sep="")
else:
    print("Please try again with number from 1 to 9")
