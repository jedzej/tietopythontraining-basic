numberOfZeroes = 0

for i in range(int(input("How many numbers you want to type? "))):
    if int(input("Type the number "+ str(i+1) + "  ")) == 0:
        numberOfZeroes += 1
print("You have " + str(numberOfZeroes) + " zeroes.")