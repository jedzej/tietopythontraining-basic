second_largest, largest, i = 0, 0, 0
while True:
    n = abs(int(input("Enter number: ")))
    if n > largest:
        second_largest, largest = largest, n
    elif second_largest < n:
        second_largest = n
    i += 1
    if n == 0 and i > 2:
        break
print(second_largest)
