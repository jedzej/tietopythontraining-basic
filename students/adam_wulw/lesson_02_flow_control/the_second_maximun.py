max_old = 0
max_current = 0
while (1):
    num = int(input('Enter number\n'))
    if num == 0:
        break
    max_old = max_current
    max_current = max(num, max_current)
    if (max_current == num):
    max_last = max_old
    else:
        max_last = max(max_last, num)
print(max_last)
