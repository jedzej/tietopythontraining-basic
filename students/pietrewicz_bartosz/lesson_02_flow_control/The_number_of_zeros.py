# Read the number of integers (N)
N = int(input())
# Read the N integers in a loop and check how many of them are equal to 0
zeros = 0
for i in range(N):
    x = int(input())
    if x == 0:
        zeros += 1
print(zeros)
