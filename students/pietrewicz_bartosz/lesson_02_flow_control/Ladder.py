# Read an integer:
n = int(input())
# Print a ladder for the given n
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, sep='', end='')
    print()
