max = 0
num_max = 0
el = -1

while el != 0:
    el = int(input())
    if el > max:
        max, num_max = el, 1
    elif el == max:
        num_max += 1 
       
print(num_max)
