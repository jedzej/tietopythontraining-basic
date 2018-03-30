# Read integers until 0 is entered and remember count of integers equal to the
# maximum
count = 0
maximum = 0
n = 1
while n != 0:
    n = int(input())
    if n > maximum:
        maximum = n
        count = 1
    elif n == maximum:
        count += 1
print(count)
