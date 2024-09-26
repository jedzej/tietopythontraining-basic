maximum = 0
howManyMaximumNumbers = 0
counter = 1

print("Type the numbers. Stop with 0.")

while counter != 0:
    counter = int(input())
    if counter > maximum:
        maximum, howManyMaximumNumbers = counter, 1
    elif counter == maximum:
        howManyMaximumNumbers += 1
print("Maxium number appears: " + str(howManyMaximumNumbers))