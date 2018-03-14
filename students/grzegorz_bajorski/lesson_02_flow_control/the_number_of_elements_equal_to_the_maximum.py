maximum = 1
count = 0
x = 1

while x != 0:
    x = int(input())
    if x > maximum:
        maximum = x
        count = 1
    elif x == maximum:
        count += 1
print(count)

