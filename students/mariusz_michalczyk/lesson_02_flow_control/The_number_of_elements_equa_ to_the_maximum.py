# NOT FINISHED

equal_nrs, largest, i = 0, 0, 0
while True:
    n = abs(int(input()))
    if n > largest:
        largest = n
    if n == largest:
        equal_nrs += 1
        print("+")
    if n == 0:
        break
print(equal_nrs)
