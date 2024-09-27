#In bowling, the player starts wtih 10 pins at the far end of a lane. The object is to knock all the pins down. For this exercise, the number of pins and balls will vary. Given the number of pins N and then the number of balls K to be rolled, followed by K pairs of numbers (one for each ball rolled), determine which pins remain standing after all the balls have been rolled. The balls are numbered from 1 to N (inclusive) for this situation. The subsequent number pairs, one for each K represent the start to stop (inclusive) positions of the pins that were knocked down with each role. Print a sequence of N characters, where "I" represents a pin left standing and "." represents a pin knocked down.

print("Enter the number of pins and rolls:")
N, K = [int(i) for i in input().split()]

pins = ["I" for i in range(N)]

for i in range(K):
    start, stop = [int(i) for i in input().split()]
    for p in range(start-1, stop):
        del pins[p]
        pins.insert(p, ".")

for i in range(len(pins)):
    print(pins[i], end="")
