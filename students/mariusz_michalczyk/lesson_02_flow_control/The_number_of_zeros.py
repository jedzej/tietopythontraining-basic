size = int(input("How many numbers you want to enter: "))
zeros = 0
id = (size+1) - size
while size:
    number = int(input("Enter number " + str(id) + ": "))
    if number == 0:
        zeros += 1
    size -=1
    id += 1
print (zeros)