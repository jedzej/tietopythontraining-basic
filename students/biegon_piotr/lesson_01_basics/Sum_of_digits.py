print("Sum of digits\n")

number = int(input("Enter a three-digit number: "))

print("\nSum of a three-digit number is:", (sum([int(digit) for digit in str(number)])))