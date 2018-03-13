# Read an integer:
# a = int(input())
# Print a value:
# print(a)

zeros = 0

for i in range(int(input())):
    if int(input()) == 0:
        zeros += 1

print(zeros)