zeroes = 0
N = int(input())
for i in range(N):
    number = int(input())
    if number == 0:
        zeroes += 1
print(zeroes)
