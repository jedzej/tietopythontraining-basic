n = 1
max_number = 0
max_count = 0

while n != 0:
    n = int(input())
    if n > max_number:
        max_number = n
        max_count = 1
    elif n == max_number:
        max_count += 1

print(max_count)
