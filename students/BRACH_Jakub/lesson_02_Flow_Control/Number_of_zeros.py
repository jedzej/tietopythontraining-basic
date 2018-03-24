N = int(input())
c = 0
zeros = 0
for c in range(0, N):
    number = int(input())
    if number == 0:
        zeros = zeros + 1
print(zeros)
