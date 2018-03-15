number =int(input("Enter number: "))

total = 1
for i in range(1, number + 1):
    total *= i
print ("Factorial of " + str(number) + " number is " + str(total))
