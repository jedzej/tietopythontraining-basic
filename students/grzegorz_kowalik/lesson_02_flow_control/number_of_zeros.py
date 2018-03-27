n = int(input())

zeros = 0
for _ in range(0, n):
    if input() == "0":
        zeros += 1

print(zeros)
