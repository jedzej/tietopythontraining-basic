maximum = 0
counter = 0
x = 1

while x:
    x = int(input())
    if x > maximum:
        maximum = x
        counter = 0
    if x == maximum:
        counter += 1

print(counter)
