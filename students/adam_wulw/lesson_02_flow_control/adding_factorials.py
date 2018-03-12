n = int(input('Enter number\n'))
ret = 1
ret_sum = 1
for i in range(1, n):
    ret = (i + 1) * ret
    ret_sum = ret_sum + ret
print(ret_sum)
