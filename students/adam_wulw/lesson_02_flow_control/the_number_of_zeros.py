iters = int(input('Enter number\n'))
count = 0
for i in range(iters):
    num = int(input('Enter number\n'))
    if (not num):
        count = count + 1
print(count)
