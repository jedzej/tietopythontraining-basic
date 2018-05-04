N, K = [int(s) for s in input().split()]

pins = ["I"] * N

for i in range(K):
    start, stop = [int(s) for s in input().split()]
    for j in range(start - 1, stop):
        pins[j] = "."

print("".join(pins))
