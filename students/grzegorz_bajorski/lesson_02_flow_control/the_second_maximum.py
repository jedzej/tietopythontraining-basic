maximum = 0
max_second = 0
x = 1

while x != 0:
    x = int(input())
    if x > maximum:
        max_second = maximum
        maximum = x
    elif x < maximum and x > max_second:
        max_second = x

print(max_second)

