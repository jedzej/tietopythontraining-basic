print("The number of elements equal to the maximum\n")

max1 = 0
counter = 0

while True:
    n = int(input("Enter the number: "))
    if n == 0:
        break
    if n > max1:
        max1 = n
        counter = 1
    elif n == max1:
        counter = counter + 1

print("\nIn the given sequence is {:d} elements equal to the maximum.".format(counter))
