n = int(input('Enter number\n'))
ret = 1
for i in range(1, n):
    ret = (i + 1) * ret
print('{:d}! = {:d}'.format(n, ret))
