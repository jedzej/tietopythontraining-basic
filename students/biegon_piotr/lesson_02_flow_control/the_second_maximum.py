print("The second maximum\n")

max1 = 0
max2 = 0

while True:
    n = int(input("Enter the number: "))
    if n == 0:
        break
    if n > max1:
        max2 = max1
        max1 = n
    elif (n > max2) and (n < max1):
        max2 = n

print("\nThe value of the second largest element is: {:d}".format(max2))
