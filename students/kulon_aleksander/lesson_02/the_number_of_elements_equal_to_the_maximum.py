max = 0
counter = 0
x = 1

while x:
    x = int(input())
    if x > max:
        max = x
        counter = 0
    if x == max:
        counter += 1
        
print(counter)
